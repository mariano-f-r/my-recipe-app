from django import forms
from .models import Comment, Recipe

class CommentForm(forms.ModelForm):
  class Meta:
      model = Comment
      fields = [
        'content',
      ]
      widgets = {
        'content': forms.Textarea(attrs={'cols': 20, 'rows': 4}),
      }

class RecipeForm(forms.ModelForm):
  class Meta:
    model=Recipe
    fields = [
      'name',
      'description',
      'prep_time',
      'difficulty',
      'servings'
    ]