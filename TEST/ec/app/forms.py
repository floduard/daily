from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class':'form-control', 'placeholder':'Password'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class':'form-control', 'placeholder':'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PasswordChangeForm(PasswordChangeForm):
    pass


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'mobile', 'state','zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'locality': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Locality'}),
            'city' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
           'mobile': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile'}),
           'state': forms.Select(attrs={'class':'form-control', 'placeholder':'State'}),
            'zipcode': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}),
        }

