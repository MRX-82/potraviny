from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
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
    return render(request, "enter_shop.html")