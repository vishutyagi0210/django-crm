from django.shortcuts import redirect, render
from website import forms
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout


def home(request):
    if request.method == 'POST':
        form = forms.SignInForm(request , data=request.POST)
        if form.is_valid():
           login(request , form.get_user()) 
           messages.success(request , "You are successfully logged in brother!!")
           return redirect('home')
        else:
            return redirect('home')
    else:
        form = forms.SignInForm()
        return render(request , 'home.html' , {'form':form})
    
def logout_user(request):
    logout(request)
    messages.success(request , "You successfully logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "You are successfully register")
            return redirect('home')
        else:
            messages.success(request , 'please check your password again and make sure its a storng one')
            return render(request , 'register.html' , {'form':form})
    else:
        form = forms.SignUpForm()
        return render(request , 'register.html' , {'form':form})
