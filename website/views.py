from django.shortcuts import get_object_or_404, redirect, render
from website import forms
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from website import models


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
        queryset = models.Record.objects.all()
        return render(request , 'home.html' , {'form':form , 'records':queryset})
    
def logout_user(request):
    logout(request)
    messages.success(request , "You successfully logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request , "You are successfully register")
            login(request , user)
            return redirect('home')
        else:
            messages.success(request , 'please check your password again and make sure its a storng one')
            return render(request , 'register.html' , {'form':form})
    else:
        form = forms.SignUpForm()
        return render(request , 'register.html' , {'form':form})

def record_data(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.RecordDataForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "your data is successfully stored")
                return redirect('home')
            else:
                messages.success(request , "something went wrong please try again")
                return render(request , 'record_data.html', {'form':form})
        else:
            form = forms.RecordDataForm()
            return render(request , 'record_data.html',{'form':form})
    else: 
        messages.success(request , "first logg in then came")
        return redirect('home')
    
def update_record(request , pk):
    user = get_object_or_404(models.Record , pk=pk)
    form = forms.RecordDataForm(instance=user)
    
    if(request.method=="POST"):
        udpated_form = forms.RecordDataForm(request.POST , instance=user)
        if udpated_form.is_valid():
            udpated_form.save()
            messages.success(request , "successfully updated")
            return redirect('home')
    else:
        return render(request , 'record_data.html',{'form':form})
    
def delete_data(request , pk):
    object_del = get_object_or_404(models.Record , pk=pk)
    object_del.delete()
    return redirect('home')