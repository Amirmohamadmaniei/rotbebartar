from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from account import forms
from user.models import CustomUser
from . import mixins


class LoginView(generic.FormView):
    template_name = 'account/Login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def form_valid(self, form):
        user = CustomUser.objects.get(phone=form.cleaned_data['phone'])
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class RegisterView(generic.FormView):
    template_name = 'account/Register.html'
    form_class = forms.RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = CustomUser.objects.create_user(phone=form.cleaned_data['phone'],
                                              password=form.cleaned_data['password'])
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class UserProfileView(mixins.RequireSelfUser, generic.View):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)

        if user.type == 'student':
            consultant = user.consultant
            return render(request, 'account/student_profile.html', {'consultant': consultant})

        students = user.students
        return render(request, 'account/consultant_profile.html', {'students': students})
