from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(),name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/new', views.RecipeCreateView, name='recipe-create'),
    path('recipes/<int:pk>/delete', views.RecipeDeleteView.as_view(), name='recipe-delete')
    # path('recipes/new', views.RecipeCreateView.as_view(), name='recipe-create')
    # path('recipes/<str:pk>', views.recipe_detail_view, name='recipe-detail')
]
