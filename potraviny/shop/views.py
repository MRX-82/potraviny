from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm, EnterShop, AddProduct, BuyProduct
from .models import User, Product
from .logika import backet, payment
import re

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
    all_products = Product.objects.all()
    form = BuyProduct()
    product_back=[]
    product_my_back=[]
    for prod in all_products:
        product_back.append(prod.name)
    if request.method == "POST":
        new_product = request.POST.getlist("my_product")
        id.my_product = new_product
        id.save(update_fields = ["my_product"])
        return redirect(f"../potraviny_shop/{user_id}")
        #return render(request, "back_form.html", {"user_id": user_id, "new_product": new_product})
    else:
        return render(request, "potraviny_shop.html", {"product_back": product_back, "user_name": user_name, "user_id": user_id, "all_products": all_products, "form": form})

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

def add_product(request, user_id):
    """
    This is function for add Product. Only for Admin
    :param request:
    :param user_id:
    :return:
    """
    id = User.objects.get(id=user_id)
    user_name = id.name
    if request.method == "POST":
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        articl = request.POST.get('articl')
        image = request.POST.get('image')
        new_product = Product.objects.create(name=name, cost=cost, articl=articl, image=image)
        new_product.save()
        return render(request, "my_admin.html")
    else:
        userform = AddProduct()
        return render(request, "add_product.html", {"form": userform, "user_name": user_name})

def back_form(request, user_id):
    """
    PayMent products
    :param request:
    :param user_id:
    :return:
    """
    user = User.objects.get(id=user_id)
    my_product = user.my_product
    my_product, cost_products = backet(my_product)
    my_cost = user.cash
    messange = payment(cost_products, my_cost, user_id)


    return render(request, "back_form.html", {"my_product": my_product, "user_name": user.name, "cost_products": cost_products[0], "my_cash": user.cash, "messange": messange})

