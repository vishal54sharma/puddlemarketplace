from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    username = forms.CharField(max_length=50,label="",required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email = forms.EmailField(max_length=100,label="",required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']


# class LoginForm(UserCreationForm):
#     email = forms.EmailField(max_length=100,label="",required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
#     class Meta:
#         model=User
#         fields=['email','password1']
        