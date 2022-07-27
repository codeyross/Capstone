from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('recipes', views.recipe_list, name='recipe_list'),
    path('detail/<int:pk>', views.user_detail, name='user_detail'),
    path('recipe/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('paypal-reverse', views.paypal_reverse, name='paypal-reverse'),
    path('paypal-cancel', views.paypal_cancel, name='paypal-cancel'),
    path('home', views.home, name='home'),
    path('user/new', views.user_create, name='user_create'),
    path('recipe/new', views.recipe_create, name='recipe_create'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),

]