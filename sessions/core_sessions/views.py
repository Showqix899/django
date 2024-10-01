from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
# Create your views here.


#get the product that are in database
def product_list(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,"home.html",context)

#adding to the data base
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)

    #get the cart from the session, if not present create an empty dictionary
    cart=request.session.get('cart',{})
    #add the product to the cart
    if str(product_id) in cart:
        cart[str(product_id)]['quantity']+=1
    else:
        cart[str(product_id)]={'name':product.name,'price':float(product.price),'quantity':1}

    #save the cart back to session
    request.session['cart']=cart

    #after adding to cart return to home page
    return redirect('home')

#showing the view cart
def view_cart(request):
    cart=request.session.get('cart',{})
    context={'cart':cart}
    return render(request,'view_cart.html',context)

#to increase quantity of a product

def increase_quantity(request,product_id):

    #get the current session
    cart=request.session.get('cart',{})
    if str(product_id) in cart:
        cart[str(product_id)]['quantity']+=1

    #save the updated cart back to the session
    request.session['cart']=cart

    return redirect('view_cart')

#to decrease qunatity of a product
def decrease_quantity(request, product_id):
    # Get the cart from the session
    cart = request.session.get('cart', {})

    # Check if the product is in the cart and its quantity is greater than 1
    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            # If quantity is 1, remove the item from the cart
            del cart[str(product_id)]

    # Save the updated cart back to the session
    request.session['cart'] = cart

    return redirect('view_cart')

