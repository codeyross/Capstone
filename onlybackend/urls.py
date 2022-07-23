from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('recipes', views.recipe_list, name='recipe_list'),
    path('detail/<int:pk>', views.user_detail, name='user_detail'),
]