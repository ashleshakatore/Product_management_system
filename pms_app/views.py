from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.

def product(request):
    if request.method=="POST":
        n=request.POST['name']
        p=request.POST['price']
        q=request.POST['quantity']
        c=request.POST['category']
        print(n,p,q,c)
        obj=Product.objects.create(name=n,price=p,quantity=q,category=c)
        obj.save()
        return redirect('/')
    return render(request,'product.html')

def table(request):
    products=Product.objects.all()
    print(products)
    context={}
    context['products']=products
    for i in products:
        print(i.name,i.price,i.quantity,i.category)
        
    return render(request,'table.html',context)
    
def delete(request,pid):
    products=Product.objects.filter(id=pid)
    products.delete()
    return redirect('/')

def edit(request,pid):
    if request.method =="GET":
        products=Product.objects.get(id=pid)
        context={}
        context['products']=products
        return render(request,'edit.html',context)
    elif request.method == "POST":
        n=request.POST['name']
        p=request.POST['price']
        q=request.POST['quantity']
        c=request.POST['category']
        product=Product.objects.filter(id=pid)
        product.update(name=n,price=p,quantity=q,category=c)
        return redirect('/')



