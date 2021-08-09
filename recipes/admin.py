from django.contrib import admin
from .models import Recipe, Ingredient, Step, Comment
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(Comment)