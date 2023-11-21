"""
This modul do it difficult mathematic functions
"""
from .models import User, Product
import re

def backet(my_product):
    """
    Correction product in backet
    """
    select_products = re.sub(r'[^\w\s]', '', my_product)
    m_product = []
    cost_products = [0]
    for i in select_products:
        if i != " ":
            i = int(i)
            m_product.append(i)
    my_product = Product.objects.filter(articl__in=m_product)
    for number in my_product:
        cost_products[0] += number.cost
    return (my_product, cost_products)

def payment(cost_products, my_cost, user_id):
    """
    Checking the availability of funds and the possibility of payment
    :return:
    """
    user = User.objects.get(id = user_id)
    result = my_cost - cost_products[0]
    if result < 0:
        message = ("Don't have money")
        return (message)
    else:
        message = ("Successfully paid, cost shopping ="+str(cost_products[0]))
        user.cash = result
        user.save(update_fields=["cash"])
        return (message)

def money(id, cash):
    user = User.objects.get(id = id)
    user.cash = cash
    user.save(update_fields=["cash"])
    message = "GOOD WORK"
    return (message)

def user_delete(id):
    user = User.objects.get(id = id)
    user.delete()
    messange = "User Delete"
    return (messange)

def product_delete(id):
    product = Product.objects.get(id = id)
    product.delete()
    messange = "Product Delete"
    return (messange)
