from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
from grp.forms import RegisterForm, ProfileForm, CicleForm
from django.contrib import messages
from grp.models import Profile
from django.urls import reverse
from grp import models

class LoginView(TemplateView):
    template_name = "registration/login.html"


    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/profile")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class HomeView(TemplateView):
    template_name = "home.html"

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                if User.objects.filter(username=form.cleaned_data['username']).exists():
                    messages.error(request, u"Пользователь с таким именем уже есть, введите новое имя")
                    return redirect("/register")
                elif User.objects.filter(email=form.cleaned_data['email']).exists():
                    messages.error(request, u"Пользователь с таким email уже есть, введите новый email ")
                    return redirect("/register")
                self.create_new_user(form)
                messages.success(request, u"Вы успешно зарегистрировались!")
                return redirect("/login")

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def create_new_user(self, form):
        email = None
        if 'email' in form.cleaned_data:
            email = form.cleaned_data['email']
        User.objects.create_user(form.cleaned_data['username'], email, form.cleaned_data['password'])


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class CicleList(ListView):
    model = models.Cicle
    queryset = models.Cicle.objects.all()
    context_object_name = 'cicle'

class ProfileView(TemplateView):
    template_name = "registration/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect(reverse("edit_profile"))
        form = CicleForm(request.POST)
        return render(request, self.template_name, {'selected_user': request.user,
                                                    'form': form
                                                    }
                      )

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None


    def new_cicle(request):
        if request.method == 'POST':
            cicle = CicleForm(request.POST)
            if cicle.is_valid():
                new_cicle = cicle.save(commit=False)
                new_cicle.user = request.user
                new_cicle.save()
                return redirect(cicle)


class EditProfileView(TemplateView):
    template_name = "registration/edit_profile.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.get_profile(request.user))
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=self.get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, u"Профиль успешно обновлен!")
                return redirect("/profile")
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None









