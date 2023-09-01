from django.shortcuts import render,get_object_or_404,redirect
from .form import NewItemForm,EditItemForm
from .models import Item,Category
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def detail(request, pk):
    item = get_object_or_404(Item,id=pk)
    relateditems = Item.objects.filter(category = item.category,is_sold=False).exclude(id=pk)[0:3]
    return render(request,'item/detail.html',{'item':item,'relateditems':relateditems})


@login_required()
def new(request):
    form = NewItemForm()

    if request.method=='POST':
        item = NewItemForm(request.POST,request.FILES)
        if item.is_valid():
            item = item.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request,"Successfully created new item")
            return redirect('detail',pk = item.id)
        else:
            messages.error(request,item.errors)
    else:
        return render(request,'item/form.html',{'form':form,'title':'New Item'})


@login_required()
def searchItem(request):

    if request.GET.get('q')!=None:
        q=request.GET.get('q')  
    else:
        q=''

    

    items = Item.objects.filter(Q(category__name__icontains=q)|Q(name__icontains=q)|Q(description__icontains=q))
    categories =Category.objects.all()

    return render(request,'item/searchItem.html',{'items':items,'categories':categories})





@login_required()
def deleteItem(request,pk):
    
    item = get_object_or_404(Item,id=pk,created_by=request.user)  

    item.delete()
    messages.success(request,"Item deleted successfully!!!")
    return redirect('allItems')


@login_required()
def editItem(request,pk):
    item = get_object_or_404(Item,id=pk,created_by=request.user) 

    form = EditItemForm(instance=item)

    if request.method=='POST':

        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            # item = item.save(commit=False)
            
            # item.is_sold=
            form.save()
            messages.success(request,"Successfully edited item")
            return redirect('detail',pk = item.id)
        else:
            messages.error(request,form.errors)
    else:
        return render(request,'item/form.html',{'form':form,'title':'Edit Item'})