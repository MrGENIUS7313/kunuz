from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, UpdateView
from .models import User
from .forms import RegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request, 'registration/register.html', context)

    def post(self, request): 
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        context = {
            'form' : form
        }
        return redirect('account:login')


class MyProfileView(View):
    def get(self, request):
        profile = User.objects.filter(username=self.request.user)
        return render(request, 'my_profile.html', {'profile': profile})


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'registration/user_update.html'
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs['id'])

    def get_success_url(self) -> str:
        id = self.kwargs['id']
        return reverse("account:my_profile")
    
    def test_func(self) -> bool | None:
        obj = User.objects.filter(username=self.request.user)
        if obj:
            return True
        elif self.request.user.is_superuser:
            return True
        else: 
            return  False


