from django.contrib import admin
from .models import Chef
from .models import Recipes
# Register your models here.
admin.site.register(Chef)
admin.site.register(Recipes)