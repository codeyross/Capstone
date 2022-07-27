

from django.shortcuts import redirect, render
from .models import User, Recipes, Comments
from django.views.generic import FormView, TemplateView
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.contrib import messages
from .forms import UserForm, RecipeForm
from PIL import Image, ImageFilter
# Create your views here.



def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, '/Users/rosswarren/GA-COURSE-WORK/capstone_project/backend/onlybackend/templates/user_form.html', {'form': form})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('recipe_detail', pk=user.pk)
    else:
        form = RecipeForm()
    return render(request, '/Users/rosswarren/GA-COURSE-WORK/capstone_project/backend/onlybackend/templates/recipe_form.html', {'form': form})

def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
        return render(request, 'user_form.html', {'form': form})

def recipe_edit(request, pk):
    recipe = Recipes.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
        return render(request, 'recipe_form.html', {'form': form})
            


def index(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECIEVER_EMAIL,
        'amount': '20.00',
        'item_name': 'Product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-reverse")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',

    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    print(context)
    return render(request, 'home.html', context)

def paypal_reverse(request):
    messages.succes(request, 'Purchase successful')
    return redirect('home')

def paypal_cancel(request):
    messages.error(request, 'Your order has been cancelled')
    return redirect('home')


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def recipe_list(request):
    recipes = Recipes.objects.all()
    print(recipes)
    return render(request, 'recipe_list.html', {'recipes': recipes})

def comments_list(request):
    comments = Comments.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    print(user.profile_pic)
    return render(request, 'user_detail.html', {'user': user})

def recipe_detail(request, pk):
    recipe = Recipes.objects.get(id=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
    
def user_delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('user_list')

def recipe_delete(request, pk):
    Recipes.objects.get(id=pk).delete()
    return redirect('recipe_list')    