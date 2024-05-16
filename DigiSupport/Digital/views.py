from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import NetAuthorizationRequest, Post
from .forms import SignupForm, LoginForm, NetAuthorizationRequestForm

def home(request):
    return render(request, 'Digital/home.html')

def request_page(request):
    if request.method == 'POST':
        form = NetAuthorizationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Request submitted successfully")
            return HttpResponseRedirect('/request/')  # Redirect to a success page or the same form
    else:
        form = NetAuthorizationRequestForm()
    return render(request, 'Digital/request.html', {'form': form})

def contact(request):
    return render(request, 'Digital/contact.html')

def RPA(request):
    return render(request, 'Digital/RPA.html')

def report(request):
    requests = NetAuthorizationRequest.objects.all()
    return render(request, 'Digital/report.html', {'requests': requests})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request=request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/home/')
                else:
                    messages.error(request, "Invalid username or password")
        else:
            form = LoginForm()
        return render(request, 'Digital/login.html', {"form": form})
    else:
        return HttpResponseRedirect('/request/')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign up successful. Please log in.")
            return HttpResponseRedirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'Digital/signup.html', {"form": form})

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return HttpResponseRedirect('/')
