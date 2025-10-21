from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Пароли не совпадают")
            redirect('register')
        
        print(User.objects.filter(username=username).exists())

        if User.objects.filter(username=username).exists():
            messages.error(request, "Пользователь с таким именем уже существует.")
            redirect('register')

        User.objects.create_user(username=username, password=password)
        redirect("login")
    
    return render(request, "auth/register.html")


def login_custom(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("main")
    else:
        messages.error(request, "Пользователь не найден или неверный пароль")

    return render(request, "auth/login.html")


