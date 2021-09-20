from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.core.mail import send_mail
from .forms import UserForm

# Create your views here.
def registerView(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,'Account/RegisterForm.html', {'form':form})

def loginView(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'Account/LoginForm.html',{})

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def changePasswordView(request):
    form=PasswordChangeForm(request.user)
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed Successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error bellow')

    return render(request, 'Account/ChangePassword.html',{'form':form})

def mailSendView(request):
    print('In send mail view')
    send_mail('Test Mail',                      # Subject
              'This is test mail',              # Message
              'dr.kalamtesting@gmail.com',      # from mail_id
              ['bansodpratik123@gmail.com'],    # To mail_id
              fail_silently=False
              )
    return HttpResponse('Mail Ssent Successfully.')
