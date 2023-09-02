from django.shortcuts import render,get_object_or_404,redirect
from  item.models import Item
from .models import Conversation
from .form import ConversationMessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def new_Conversation(request,pk):
    item = get_object_or_404(Item,id=pk)
    
    if item.created_by == request.user:
        return redirect('detail',pk=pk)
    
    conversations = Conversation.objects.filter(item=item,members__in=[request.user.id])

    if conversations:
        pass # redirect to converstaions

    if request.method=='POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            return redirect('detail',pk=pk)
    else:
        form = ConversationMessageForm()
        return render(request,'conversation/new_conversation.html',{'form':form})
    

@login_required()
def conversationDetail(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    form = ConversationMessageForm()
    if request.method == 'POST':
        message  = ConversationMessageForm(request.POST)
        if message.is_valid():
            conversation_message =message.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect('messages',pk=pk)
    else:    
        return render(request,'conversation/conversation_detail.html',{'conversation':conversation,'form':form})


@login_required()
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request,'conversation/inbox.html',{'conversations':conversations})