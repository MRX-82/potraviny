from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm, EnterShop
from .models import User

def index(request):
    return render(request, "index.html")


def registration_form(request):
    """
    form for registration new users
    :param request:
    :return:
    """
    if request.method == "POST":
        name = request.POST.get("name")
        login = request.POST.get("login")
        number = request.POST.get("number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        registration_info = User.objects.create(name=name, login=login, number=number, email=email, password=password)
        registration_info.save()
        return HttpResponse(f"list{name}{login}{number}{email}{password}")
    else:
        userform = UserForm()
        return render(request, "registration_form.html", {"form": userform})

def enter_shop(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        user = User.objects.filter(login=login).exists()
        if user == False:
            return HttpResponse(f"Login Error")
        else:
            user = User.objects.get(login=login)
            user_id = user.id
            if user.password == password and user.login == login:
                return redirect(f"../potraviny_shop/{user_id}")
            else:
                return HttpResponse(f"Password Error")
    else:
        userform = EnterShop()
        return render(request, "enter_shop.html", {"form": userform})

def potraviny_shop(request, user_id):
    id = User.objects.get(id=user_id)
    user_id = id.name
    return render(request, "potraviny_shop.html", {"user_id": user_id})

def my_office(request):
    return render(request, "my_office.html")