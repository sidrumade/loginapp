from django import forms
from django.contrib.auth.models import User
from loginapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

    #let override default password field
    password = forms.CharField(widget=forms.PasswordInput())

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        
