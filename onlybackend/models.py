

from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    chef = models.CharField(max_length=500)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    user_permissions = models.CharField(max_length=1000)
    profile_pic = models.TextField()
    nationality = models.CharField(max_length=200)
    about = models.CharField(max_length=5000)

    def __str__(self):
        return self.chef
#may need to add chef to recipe class for foreign key for proper link/naming

class Recipes(models.Model):
    user = models.ForeignKey(
                    User, 
                    on_delete=models.CASCADE, 
                    related_name='recipes',
                    )
    recipe_name = models.CharField(max_length=1000, default='no recipe name')
    picture = models.TextField()
    recipe_description = models.CharField(max_length=1000, default='no recipe description')
    ingredients = models.CharField(max_length=5000, default='no ingredients listed')
    recipe = models.CharField(max_length=10000, default='no recipe listed')
 
    def __str__(self):
        return self.recipe_name

class Comments(models.Model):
    recipe_name = models.ForeignKey(
                    Recipes,
                    on_delete=models.CASCADE,
                    related_name='comments'
                    )
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)