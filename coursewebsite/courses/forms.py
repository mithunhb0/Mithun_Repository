from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=20,required=True)
    last_name = forms.CharField(max_length=20,required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',]
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            return email
        
        if user is not None:
            raise forms.ValidationError('Email already exist')
    
    
class SigninForm(AuthenticationForm):
    username = forms.EmailField(required=True, label='Email')

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email=email)
            result = authenticate(username=user.username, password=password)

            if result is not None:
                return result
            else:
                raise forms.ValidationError("Email or password Invalid")
        except:
            raise forms.ValidationError("Email or password Invalid")
    