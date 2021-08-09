from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, Step, Comment
from .forms import CommentForm, RecipeForm

# Create your views here.

# def home(request):
#     context = {
#         'recipes': Recipe.objects.all(),
#         'recipecount':Recipe.objects.all().count(),
#         'usercount':User.objects.all().count(),
#     }
#     return render(request, 'home.html', context)

class AboutView(generic.TemplateView):
    template_name = 'recipes/about.html'

class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by=10
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipecount'] = Recipe.objects.all().count()
        context['usercount'] = User.objects.all().count()
        return context

class RecipeDetailView(generic.DetailView):
    model = Recipe
    context_object_name='recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.filter(recipe=self.get_object().pk)
        context['steps'] = Step.objects.filter(recipe=self.get_object().pk)
        context['comments'] = Comment.objects.filter(recipe=self.get_object().pk)
        context['form'] = CommentForm
        return context

    def post(self, *args, **kwargs):
        self.recipe = self.get_object(self.get_queryset())
        form = CommentForm(self.request.POST)
        if form.is_valid():
            form.instance.author=self.request.user
            form.instance.recipe = self.recipe
            form.save()
            return HttpResponseRedirect(self.model.get_absolute_url(self.recipe))
        else:
            context = self.get_context_data(**kwargs)
            context['form']=form
            return self.render_to_response(context)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Recipe
    success_url='/'
    def test_func(self):
        recipe=self.get_object()
        if self.request.user==recipe.author:
            return True
        return False

@login_required
def RecipeCreateView(request):
    context = {}
    if request.method == 'POST':
        requestdict = request.POST
        recipedict = {}
        ingredientlist = []
        steplist = []
        # Loops through QueryDict and looks for keys
        for i in requestdict:
            if not 'csrf' in i:
                if 'ingredient' not in i and 'step' not in i:
                    recipedict[i] = requestdict[i]
                elif 'ingredient' in i:
                    ingredientlist.append(requestdict[i])
                elif 'step' in i:
                    step = [int(i[5:]),requestdict[i]]
                    steplist.append(step)

        recipeform = RecipeForm(recipedict, instance=request.user)
        ingredientsvalid = None
        stepsvalid=None
        for i in ingredientlist:
            ingredienterrors = []
            if len(i)<101 and len(i)>0:
                ingredientsvalid=True
            else:
                if len(i)>100:
                    ingredienterrors.append(f'Ingredient "{i}" is {len(i)-100} too long\n')
                elif len(i)<1:
                    ingredienterrors.append('You can\'t leave ingredients blank')

        for i in steplist:
            steperrors = []
            if len(i[1])>0:
                stepsvalid=True
            else:
                steperrors.append('You can\'t leave steps blank')
                stepsvalid=False
        if recipeform.is_valid() and ingredientsvalid and stepsvalid:
            # The following is probably the worst practice used in this web app, however at this point I have failed to find anything that works. It creates then saves a new instance of each model (Recipe, Ingredient Step)
            recipeinstance = Recipe(name=recipedict['name'],description=recipedict['description'], prep_time=recipedict['prep_time'], difficulty=recipedict['difficulty'], servings=recipedict['servings'], author=request.user)
            recipeinstance.save()
            for i in ingredientlist:
                ingredientinstance = Ingredient(recipe=recipeinstance, ingredient=i)
                ingredientinstance.save()
            for i in steplist:
                stepinstance=Step(recipe=recipeinstance,step=i[1], number=i[0])
                stepinstance.save()
                stepinstance=None
            messages.success(request,'Your recipe has been successfully created')
            return redirect('recipe-detail', pk=recipeinstance.pk)
        else:
            context['recipeformerrors']=recipeform.errors
            context['ingredientformerrors']=ingredienterrors
            context['stepformerrors']=steperrors
            # This better not slow down the app at runtime or in production

    return render(request, template_name='recipes/recipe_form.html', context=context)




# class RecipeCreateView(LoginRequiredMixin,generic.CreateView):
#     model = Recipe
#     fields = [
#         'name',
#         'description',
#         'prep_time',
#         'difficulty',
#         'servings',
#     ]


#     def form_valid(self, form):
#         form.instance.author=self.request.user
#         return super().form_valid(form)


# def recipe_detail_view(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
#     context = {
#         'recipe': recipe,
#         'ingredients': Ingredient.objects.filter(recipe=pk)
#         }
#     return render(request, 'recipes/recipe_detail.html', context=context)