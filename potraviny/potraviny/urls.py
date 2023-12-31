"""
URL configuration for potraviny project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index),
    path('registration_form/', views.registration_form),
    path('enter_shop/', views.enter_shop),
    path('potraviny_shop/<int:user_id>', views.potraviny_shop),
    path('potraviny_shop/<int:user_id>/my_office/', views.my_office),
    path('potraviny_shop/<int:user_id>/my_office/my_admin/', views.my_admin),
    path('potraviny_shop/<int:user_id>/my_office/my_admin/add_product/', views.add_product),
    path('potraviny_shop/<int:user_id>/back_form/', views.back_form),
    path('potraviny_shop/<int:user_id>/my_office/my_admin/settings_all/', views.settings_all),
    path('potraviny_shop/<int:user_id>/my_office/shoping_complete/', views.shoping_complete),
    path('potraviny_shop/<int:user_id>/my_office/my_admin/product_delete/', views.product_del),
    path('potraviny_shop/<int:user_id>/my_office/my_admin/user_delete/', views.user_del),

]
