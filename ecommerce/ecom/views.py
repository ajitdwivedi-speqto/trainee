from django.shortcuts import render,redirect
from ecom.models import product
from ecom.form import ProductForm,buyForm
from django.core.mail import send_mail,EmailMultiAlternatives


# Create your views here.

def product_list(request):
    products=product.objects.all()
    return render(request,'home.html',{'products':products})
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price= form.cleaned_data['price']
            specifications= form.cleaned_data['specifications']
            img= form.cleaned_data.get('img')
            product.objects.create(name=name,price=price,specifications=specifications,img=img)
            return redirect('home')

    else:
            form=ProductForm()
    return render (request,'form.html',{'form':form})
def edit_product(request,id):
    products=product.objects.get(id=id)

    if request.method=='POST':
        form=ProductForm(request.POST , request.FILES)
        if form.is_valid():
            products.name = form.cleaned_data['name']
            products.price= form.cleaned_data['price']
            products.specifications= form.cleaned_data['specifications']
            products.img = form.cleaned_data.get('img') 
            products.save()
            return redirect('home')
    else:
        form=ProductForm(initial={'name':products.name,'price':products.price,'specifications':products.specifications})
    return render(request,'form.html',{'form':form})
def buy_product(request,id):
    products=product.objects.get(id=id)
    if request.method=='POST':
        form=buyForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            quantity=form.cleaned_data['quantity']
            details=f"Product: {products.name}\nPrice: {products.price}\nQuantity: {quantity}\nTotal Price: {products.price * quantity}\nShipping Address: {address}"
            send_order_email(name,email,details)
             )

            return redirect('home')
    else:
        form=buyForm()
    return render(request,'form.html',{'form':form})

def send_order_email(name,email,details):
    subject = 'Your Order Confirmation'
    from_email = None  # Use default from settings
    to_email = email
    text_content = f'Thank you for your purchase, {name}!\n\nHere are your order details:\n\n{details}'
    html_content = f'<p>Thank you for your purchase, {name}!</p><p>Here are your order details:</p><pre>{details}</pre>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()



from rest_framework import viewsets
from .models import product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import NotFound, ValidationError, ParseError
from utils.ExceptionHandler import custom_exception_handler
from utils.CustomException import InvalidProductId


class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="List all courses"
    )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
           
            raise InvalidProductId()

    
