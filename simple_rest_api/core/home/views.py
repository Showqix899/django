from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PeopleSerializer,LoginSerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class RegisterAPI(APIView):
    
    def post(self, request):
        data=request.data
        serializer=RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {
                    "status": False,
                    "message": serializer.errors,
                 },
                    status=status.HTTP_400_BAD_REQUEST
                )
        serializer.save()
        return Response({"status": True, "message": "User created successfully"}, status=status.HTTP_201_CREATED)
    

class LoginAPI(APIView):
    
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {
                    "status": False,
                    "message": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Authenticate user using username and password
        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if user is None:
            return Response(
                {
                    "status": False,
                    "message": "Invalid credentials",
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generate or get the auth token
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "status": True,
            "message": "User logged in successfully",
            "token": str(token)
        }, status=status.HTTP_202_ACCEPTED)





@api_view(['GET','POST','PUT'])
def index(request):
    courses={
        "course_name":"python",
        'learn':['flask','django','Tornado','FastApi'],
        'course_provider':'scaler'
    }
    #if it is a get method (GET method is sending data to client/user)
    if request.method=='GET':
        data=request.GET.get("search")
        print(data)
        print('this is GET method')
        return Response(courses)
    #if it is a POST method (POST method is extracting data from the user and send it to the backend/server)
    elif request.method=='POST':
        data=request.data
        print(data)
        print('this is POST method')
        return Response(courses)
    #if it is a PUT method ~ updation(PUT method take data from the user/client and update the particular data in the database)
    elif request.method=='PUT':
        print('this is PUT method')
        return Response(courses)


@api_view(['POST'])
def login(request):
    data=request.data
    serializer=LoginSerializer(data=data)

    if serializer.is_valid():
        data=serializer.validated_data
        print(data)
        return Response({"message": "success"})
        

    return Response(serializer.errors)



@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    #getting the existing data from the database/backend for user/cliet request
    if request.method=='GET':
        objs=Person.objects.all() # all the instance
        serializer=PeopleSerializer(objs , many = True) #serializing the data (converting query set to json)
        return Response(serializer.data) # returning the response
    
    #getting data from the user/client and save it in the backend/database
    elif request.method=='POST':
        data=request.data #getting the data
        serializer=PeopleSerializer(data = request.data) #serializing the data (converting json to query set)

        if serializer.is_valid(): #checking the serializer is_valid
            serializer.save() #saving in the data base
            return Response(serializer.data) # returning the response
        return Response(serializer.errors) #If any error
    #PUT method ~ updation(PUT method take data from the user/client and update the particular data in the database)
    elif request.method=="PUT":
        data=request.data #getting the data that's gonna be update
        serializer=PeopleSerializer(data=request.data) #serializing the fetched data to json
        if serializer.is_valid(): #checking the serializer is_valid
            serializer.save()#saving
            return Response(serializer.data) #returning response
        return Response(serializer.errors)


    #it's almost the same but there is a difference
    #when we update with PUT method it's we have defined all the other property of a model and after updation it's create a new element of the model
    #when we use PATCH we just have to define id/name or any other propery that can uniquely identify the element than define what to change. it does not
    #-> create a new element
    elif request.method=="PATCH":
        data=request.data #getting the data that's gonna be update
        obj=Person.objects.get(id=data['id']) #giving the id to change it's properthy

        serializer=PeopleSerializer(obj,data=request.data,partial=True) #serializing 
        if serializer.is_valid(): #checking for validation
            serializer.save() #saving
            return Response(serializer.data) #returung resoponse
        return Response(serializer.errors)
    #for delete
    elif request.method == 'DELETE':
        data=request.data #getting the data for deleting
        try:
            obj = Person.objects.get(id=data['id']) # specifing the id
            obj.delete() # deleted
            return Response({'messgae': 'Person is Deleted'}) #returning confirmation message
        except:
            return Response({'message':'the person you trying to delete does not exits'}) #if any error
    



########## Using Classed based view (imported APIview)



class PersonAPI(APIView):
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    def get(self,request):
        #getting all the data from the database
        objs=Person.objects.all()
        #serializing the data
        serializer=PeopleSerializer(objs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PeopleSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def put(self,request):
        data=request.data #getting the data that's gonna be update
        obj=Person.objects.get(id=data['id']) #giving the id to change it's
        #properthy
        serializer=PeopleSerializer(obj,data=request.data,partial=True) #serializing
        if serializer.is_valid(): #checking for validation
            serializer.save() #saving
            return Response(serializer.data) #returung resoponse
        return Response(serializer.errors)
    
    def patch(self , request):
        data=request.data #getting the data that's gonna be update
        obj=Person.objects.get(id=data['id']) #giving the id to change it's
        #properthy
        serializer=PeopleSerializer(obj,data=request.data,partial=True) #serializing
        if serializer.is_valid(): #checking for validation
            serializer.save() #saving
            return Response(serializer.data) #returung resoponse
        return Response(serializer.errors)
    

class PeoplViewSet(viewsets.ModelViewSet):
    serializer_class=PeopleSerializer
    queryset=Person.objects.all()

    def list(self,request):
        search= request.GET.get('search')

        queryset= self.queryset
        if search:
            queryset= queryset.filter(name__startswith=search)

        serializer=PeopleSerializer(queryset,many=True)
        return Response({'status':200,'data':serializer.data})
