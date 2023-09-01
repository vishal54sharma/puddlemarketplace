from django.shortcuts import render,redirect
from item.models import Category, Item
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully!")
            return redirect('index')
        else:
            messages.success(request,"Oops there was an error. Please try again...")
            return redirect('index')
    else:
        return render(request,'core/index.html',{'items':items,'categories':categories})

def contact(request):
    return render(request,'core/contact.html',{})

def signupUser(request):
    form =SignupForm()

    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request,username = request.cleaned_data['username'],password = request.cleaned_data['password1'])
            
            login(request,user)
            messages.success(request,"Successfully Signed Up...")
            return redirect('index')
        else:
            print(form.errors)
            messages.error(request, form.errors)

    return render(request,'core/signup.html',{'form':form})

def loginUser(request):
    # form =LoginForm()
    pass

    

def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out...")
    return redirect('index')

def aboutUs(request):
    pass