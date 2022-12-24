from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from blog.models import Surah


def index(request):
    template_name = 'front/index.html'
    context = {
        'title':'halaman index',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'halaman about',
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'front/contact.html'
    context = {
        'title':'halaman contact',
    }
    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
        print('Telah Berhasil Login')
        return redirect ('index')
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #data ditemukan
            print('username benar')
            auth_login(request, user)
            return redirect('index')
        else:
            #data tidak ditemukan
            print('username salah')
    
    context = {
        'title' : 'Form Login',
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect ('index')

def pengajian(request):
    template_name = 'front/pengajian.html'
    surah = Surah.objects.all()
    context = {
        'title':'halaman blog',
        'surah' :surah,
    }
    return render(request, template_name, context)