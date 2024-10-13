from rest_framework import serializers
from .models import Person,Color
from django.contrib.auth.models import User

#serializing the model Person (converting query set to json or vice versa)



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)


    def validate(self, data):
        if data['username']:

            if User.objects.filter(username= data['username']).exists():
                raise serializers.ValidationError("Username already exists")


        if data['email']:

            if User.objects.filter(email= data['email']).exists():
                raise serializers.ValidationError("email already exists")
            
        return data
            

    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return validated_data




class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()




class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=['name']  #to show only name  (have control what to show what not to)
class PeopleSerializer(serializers.ModelSerializer):

    color=ColorSerializer(required=False,allow_null=True) #to get data from Foreign key 
    color_info=serializers.SerializerMethodField()#adding a custom method
    class Meta:
        model=Person # data model
        fields='__all__' # field include
        # depth=1 #to show only one field (do not have controll over what can show or not)

    def get_color_info(self,obj):
        if obj.color:  # Ensure color exists before fetching its info
            color_obj = Color.objects.get(id=obj.color.id)
            return {"color_name": color_obj.name, "hex_code": "#000"}
        return None  # Return None if no color

    def validate(self,data): #checking the data that user input
        name=data.get('name')
        if name:
            special_characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`"
            if any(c in special_characters for c in data['name']):
                raise serializers.ValidationError('name can not contain special charecter')

        if data['age']< 18 :
            raise serializers.ValidationError('Age must be greater than 18')
        return data