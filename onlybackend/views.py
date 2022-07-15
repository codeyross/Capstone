
from django.shortcuts import render
from .models import User, Recipes, Comments
# Create your views here.

def user_list(request):
    users = User.objects.all()
    return render(request, '/Users/rosswarren/GA-COURSE-WORK/capstone_project/backend/onlybackend/templates/user_list.html', {'users': users})

def recipe_list(request):
    recipes = Recipes.objects.all()
    return render(request, '/Users/rosswarren/GA-COURSE-WORK/capstone_project/backend/onlybackend/templates/recipe_list.html', {'recipes': recipes})

def comments_list(request):
    comments = Comments.objects.all()
    return render(request, '/Users/rosswarren/GA-COURSE-WORK/capstone_project/backend/onlybackend/templates/comment_list.html', {'comments': comments})


    