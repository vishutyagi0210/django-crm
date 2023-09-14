from dataclasses import fields
from website import models
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    
	class Meta:
		model = User
		fields = ('username' , 'first_name' , 'last_name', 'email' , 'password1' , 'password2')
		widgets = {
            'username': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'username'}),
			'first_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'first name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'last name'}),
			'email': forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'email'}),
			'password1': forms.PasswordInput(attrs={'class':'form-control' , 'placeholder': 'Password'}),
			'password2': forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Confirm password'}),
		}

class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'username'}))
    password = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'password'}))
   
class RecordDataForm(forms.ModelForm):
    
    class Meta:
        model =  models.Record
        fields = ['first_name' , 'last_name' , 'email' , 'phone' , 'state' , 'zipcode']
        
        widgets={
			'first_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'first name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'last name'}),
			'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
			'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'phone number'}),
			'state': forms.TextInput(attrs={'class':'form-control','placeholder':'state'}),
			'zipcode': forms.TextInput(attrs={'class':'form-control','placeholder':'Postal code'}),
		}