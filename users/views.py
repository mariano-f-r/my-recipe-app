from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.views import generic
from .forms import UserRegisterForm, UserUpdateForm
from .models import Profile
from recipes.models import Recipe

# Create your views here.

def Register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# def ProfileDetailView(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     context={'profile': user}
#     return render(request, 'users/profile.html', context)

@login_required
def UserUpdateView(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-detail', pk=request.user.pk)
        else:
            messages.error(request, 'Not a valid username')
            return redirect('account-update')

    else:
        form = UserUpdateForm(instance=request.user)


    context = {
        'form': form,
    }

    return render(request, 'users/user_form.html', context)

class ProfileDetailView(generic.DetailView):
    model=User
    context_object_name='profile'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.filter(author=self.get_object().pk)

        return context

class UserRecipeListView(generic.ListView):
    model = Recipe
    paginate_by=10
    template_name = 'recipes/users_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        return Recipe.objects.filter(author=user)
    
    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['profile'] = user

        return context
    
# @login_required
# def ProfileUpdate(request):
#     if request.method == 'POST':
#         u_form=UserUpdateForm(request.POST, instance=request.user)
#         p_form=ProfileUpdateForm(request.POST, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#     else:
#         u_form=UserUpdateForm(instance=request.user)
#         p_form=ProfileUpdateForm(instance=request.user.profile)
#         messages.success(request, f'User details successfully updated.')
#         return redirect('profile-detail')
#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request, 'users/profileupdate.html', context=context) 

class ProfileUpdateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin ,generic.UpdateView):
    model = Profile
    context_object_name = 'profile'
    fields = [
        'name', 'bio' , 'email'
        ]

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

# class UserUpdateView(mixins.LoginRequiredMixin, generic.TemplateView):
