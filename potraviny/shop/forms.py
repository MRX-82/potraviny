from django import forms
from .models import User


class UserForm(forms.Form):
    """
    New user registration form
    """
    name = forms.CharField(max_length=12)
    login = forms.CharField(max_length=16)
    number = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20)


class EnterShop(forms.Form):
    """
    Store entry form.
    """
    login = forms.CharField(max_length=16)
    password = forms.CharField(max_length=20)


class AddProduct(forms.Form):
    """
    Form for adding new products
    """
    name = forms.CharField(max_length=20)
    cost = forms.IntegerField()
    articl = forms.IntegerField()
    image = forms.URLField(max_length=100)


class BuyProduct(forms.Form):
    """
    Form for purchasing goods.
    """
    User.my_product = forms.CharField()


class SettingsAll(forms.Form):
    """
    Form for adding money to users.
    """
    id = forms.IntegerField()
    cash = forms.IntegerField()


class DeleteProduct(forms.Form):
    """
    Form for deleting products.
    """
    id_product_delete = forms.IntegerField()


class DeleteUser(forms.Form):
    """
    Form for deleting users.
    """
    id_user_delete = forms.IntegerField()