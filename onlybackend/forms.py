from django import forms
from .models import User, Recipes

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('chef', 'first_name', 'last_name', 'email', 'password', 'profile_pic', 'nationality', 'about',)

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipes
        fields = ('user', 'recipe_name', 'picture', 'recipe_description', 'ingredients', 'recipe',)