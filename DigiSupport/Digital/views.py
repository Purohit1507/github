import json
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import NetAuthorizationRequest, Post
from .forms import SignupForm, LoginForm, NetAuthorizationRequestForm
from .models import Folder, File
from .forms import FolderForm, FileForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatLog

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

def save_chat_log(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        response = data.get('response')
        user = request.user if request.user.is_authenticated else None
        chat_log = ChatLog.objects.create(user=user, message=message, response=response)
        chat_log.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def Repositary(request):
    folders = Folder.objects.all()
    if request.method == 'POST':
        folder_form = FolderForm(request.POST)
        file_form = FileForm(request.POST, request.FILES)
        if folder_form.is_valid():
            new_folder = folder_form.save(commit=False)
            new_folder.created_by = request.user
            new_folder.save()
            return redirect('repositary')
        elif file_form.is_valid():
            new_file = file_form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            return redirect('repositary')
    else:
        folder_form = FolderForm()
        file_form = FileForm()
    return render(request, 'Digital/repositary.html', {
        'folders': folders,
        'folder_form': folder_form,
        'file_form': file_form
    })

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
