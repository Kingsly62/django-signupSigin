from django.shortcuts import redirect, render
from django.http import HttpResponse
from django import forms
from . models import Data

class Register(forms.Form):
   firstname = forms.CharField(max_length=80, label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Firstname'}))
   lastname = forms.CharField(max_length=80, label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Lastname'}))
   email = forms.CharField(max_length=80, label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Email'}))
   password = forms.CharField(max_length=80, label='', required=False, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
   retype_password = forms.CharField(max_length=80, label='', required=False, widget=forms.PasswordInput(attrs={'placeholder':'Retype-Password'}))

class Login(forms.Form):
   email = forms.CharField(max_length=80, label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Email'}))
   password = forms.CharField(max_length=80, label='', required=False, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

def index(request):
    return HttpResponse('Main Page')

def register(request):
    if request.method == 'POST':
      register = Register(request.POST)
      if register.is_valid():
        Firstname = register.cleaned_data['firstname']
        Lastname = register.cleaned_data['lastname']
        Email = register.cleaned_data['email']
        Password = register.cleaned_data['password']
        Retype_Password = register.cleaned_data['retype_password']

        if not Data.objects.all().filter(email = Email):
          mail = request.session['email'] = Email
          passd = request.session['password'] = Password
          Data(firstname = Firstname, lastname = Lastname, email = mail, password = passd).save()
          return redirect('/admin/')
        else:
          return render(request, 'web/register.html', {'data':register, 'alert':'<script>alert("Email Already Taken");</script>'})
    else:
      register = Register()
    return render(request, 'web/register.html', {'data':register})

def login(request):
    if request.method == 'POST':
      login = Login(request.POST)
      if login.is_valid():
        Email = login.cleaned_data['email']
        Password = login.cleaned_data['password']

        if Data.objects.all().filter(email = Email, password = Password):
          request.session['email'] = Email
          request.session['password'] = Password
          return redirect('/admin/')
        else:
          return render(request, 'web/login.html', {'data':login, 'alert':'<script>alert("Incorrect Email or Password Try Again");</script>'})
    else:
      login = Login()
    return render(request, 'web/login.html', {'data':login})

def admin(request):
    if request.session.get('email') and request.session.get('password'):
      return HttpResponse('Admin Page')
    else:
      return redirect('/login/')

def logout(request):
    try:
      del request.session['email']
      del request.session['password']
    except:
      pass
    return redirect('/login/')