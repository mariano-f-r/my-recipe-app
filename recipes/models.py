from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Recipe(models.Model):
    prep_time_choices=[
        ('short', 'Short (<20m)'),
        ('medium', 'Medium (20m-1h)'),
        ('long', 'Long (>1h)')
    ]
    difficulty_choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ]
    name=models.CharField(max_length=100, help_text='Enter the name of this recipe')
    description=models.TextField(help_text='Describe your recipe')
    date=models.DateTimeField(default=timezone.now)
    prep_time=models.CharField(max_length=6, choices=prep_time_choices, default='short')
    difficulty = models.CharField(max_length=6, choices=difficulty_choices, default='easy')
    servings=models.IntegerField(default=1)
    author= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
            
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date']

class Ingredient(models.Model):
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient=models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['ingredient']

    def __str__(self):
        return f'{self.recipe}#{self.recipe.id}: {self.ingredient}'

class Step(models.Model):
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step=models.TextField()
    number = models.IntegerField()

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.recipe.name}: {self.number}'

class Comment(models.Model):
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.author}\'s comment on {self.recipe}'