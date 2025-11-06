from django.shortcuts import render, redirect,get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *  # import model to save data

from django.contrib import messages

# Create your views here.
# def login_view(request):
#     if request.method == "POST":
#          email = request.POST.get('email')
#          password = request.POST.get('password')
#          print(email,password)
#          user = authenticate(request,username=email,password=password)
#          print(user)
#          if user:
#              login(request,user)

#          return redirect('/')

# def logout_view(request):
#     logout(request)
#     return redirect('/')


def index(request):
   
    
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        # messages.success(request,'form submitted sucessfully!')
        # messages.error(request,'something went wrong!')
        # messages.warning(request,'this is warning!')
        # messages.info(request,'just for your information !')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # user= authenticate(request,username='nileshbeck28@gmail.com', password='123456')
        # if user is not None:
        #     login(request,user)
        #     messages.success(request,f"{email}! you are logged in ")

        if email == "nileshbeck@gmail.com" and password == "123456":
            messages.success(request,f"{email}! you are logged in ")
            return redirect("home")
        else:
            messages.error(request,f"Invalid username { email } or password")
            return redirect('login')
    return render(request, "login.html")

        # User.objects.create_user(
        #     email = email,
        #     password=password
        # )

    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def add_products(request):
    if request.method == "POST":  # if form is submmited
        # get data from form inputs html

        name = request.POST.get('productName')
        cat = request.POST.get('category')
        ven = request.POST.get('vender')
        quant = request.POST.get('quantity')
        purchase = request.POST.get('purchase_price')
        selling = request.POST.get('selling_price')

    #  Save data into database using Django ORM
        product.objects.create(

            Product_name=name,
            Category=cat,
            Vender=ven,
            Quantity=quant,
            Purchase_price=purchase,
            Selling_price=selling
        )
        # after saving, redirect to home
        return redirect('add_products')
    all_category = Categories.objects.all()
    all_vender = vender.objects.values('vender_name')
    return render(request, 'add_products.html', {'category': all_category,'venders': all_vender})

def product_list(request):
    
    pro=product.objects.all()
    return render(request, 'product_list.html', {'prod': pro})

def update_product(request,pk):
    Product=get_object_or_404(product,pk=pk)
    all_category = Categories.objects.all()
    all_vender = vender.objects.values('vender_name')
    if request.method =='POST':
        update_product=request.POST.get('productName')
        update_category=request.POST.get('category')
        update_vender=request.POST.get('vender')
        update_quantity=request.POST.get('quantity')
        update_purchase=request.POST.get('purchase_price')
        update_selling=request.POST.get('selling_price')
        Product.save()
        return redirect('product_list')
    return render(request,'upadate_product.html',{'prod':Product, 'category':all_category, 'venders':all_vender })


def delete_product(request,pk):
    item=get_object_or_404(product,pk=pk)
    if request.method=="POST": #only delete if POST request
        item.delete()
    return redirect('product_list')


def delete_vender(request,pk):
    item_vender=get_object_or_404(vender,pk=pk)
    if request.method=="POST": #only delete if POST request
        item_vender.delete()
    return redirect('vender_detail')








def add_categories(request):
    if request.method == "POST":  # if the form is submitted
        # come from html and assigin to variable
        categories = request.POST.get('categories')

# model name
        Categories.objects.create(
            name=categories,   # that assing variable
        )
        return redirect('add_categories')
    return render(request, 'add_categories.html')


# view to add a new customer
def add_customer(request):
    if request.method == "POST":  # if form is submmited
        # get data from form inputs html

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')

    #  Save data into database using Django ORM
        customer.objects.create(

            name=name,
            phone=phone,
            email=email,
            address=address
        )
        # after saving, redirect to home
        return redirect('add_customer')
    # if request is GET (page load).just show the form
    return render(request, 'add_customer.html')

def delete_customer(request,pk):
    item_customer=get_object_or_404(customer,pk=pk)
    if request.method=="POST": #only delete if POST request
        item_customer.delete()
    return redirect('customer_detail')

# view for  customer list page
def customer_detail(request):
    cus=customer.objects.all()
    return render(request, 'customer_detail.html', {'cust':cus})

    # render custemer_detail.html after adding a customer




def update_customer(request,pk):
    Customer=get_object_or_404(customer,pk=pk)
    if request.method=='POST':
        Customer.name = request.POST.get('name')
        Customer.phone = request.POST.get('phone')
        Customer.email = request.POST.get('email')
        Customer.address = request.POST.get('address')
        Customer.save()
        return redirect('customer_detail')
    return render(request,'update_customer.html',{'cust':Customer})

def add_vender(request):
    
    if request.method == "POST":  # if form is submmited
        # get data from form inputs html                             
        # name=request.POST['name'] show error is data is not recieved
        name = request.POST.get('Vender_name') #not show the errror if data is not recieved put blank only
        contac = request.POST.get('Contact_person')
        phon = request.POST.get('phone')
        emmm= request.POST.get('email')
        adress = request.POST.get('address')

    #  Save data into database using Django ORM
        vender.objects.create(

            vender_name=name,
            contact_person=contac,
            Phone=phon,
            Email=emmm,
            Address=adress
        )
        # after saving, redirect to home
        return redirect('add_vender')
    # if request is GET (page load).just show the form

    return render(request, 'add_vender.html')



def vender_detail(request):
    venderss=vender.objects.all()
    return render(request, 'vender_detail.html', {'venders': venderss})

def delete_vender(request,pk):
    item_vender=get_object_or_404(vender,pk=pk)
    if request.method=="POST": #only delete if POST request
        item_vender.delete()
    return redirect('vender_detail')


def order(request):
    return render(request, 'order.html')

