from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm, EnterShop
from .models import User

def index(request):
    """
    Home page
    :param request:
    :return:
    """
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
        cash = 0
        status = 2
        registration_info = User.objects.create(name=name, login=login, number=number, email=email, password=password, cash=cash, status=status)
        registration_info.save()
        return HttpResponse(f"list{name}{login}{number}{email}{password}{cash}{status}")
    else:
        userform = UserForm()
        return render(request, "registration_form.html", {"form": userform})

def enter_shop(request):
    """
    A function for logging in to the store of authorized users,
    if there is no user or the password is incorrect, the user will receive
     a corresponding notification
    :param request:
    :return:
    """
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
    """
    Home page of the store
    :param request:
    :param user_id:
    :return:
    """
    id = User.objects.get(id=user_id)
    user_name = id.name
    user_id = id.id
    return render(request, "potraviny_shop.html", {"user_name": user_name, "user_id": user_id})

def my_office(request, user_id):
    """
    Home page of the my office
    :param request:
    :return:
    """
    id = User.objects.get(id=user_id)
    user_name = id.name
    user_status = id.status
    user_cash = id.cash
    return render(request, "my_office.html", {"user_name": user_name, "user_cash": user_cash, "user_status": user_status,
                                              "user_id": user_id})

def my_admin(request, user_id):
    """
    This is admin room
    :param request:
    :param user_id:
    :return:
    """
    id = User.objects.get(id=user_id)
    user_name = id.name
    return render(request, "my_admin.html", {"user_name": user_name})


