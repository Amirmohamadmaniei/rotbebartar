from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from account import forms
from blog.forms import BlogForm
from user.models import CustomUser, StudentProfile
from . import mixins
from . import forms
from django.contrib import messages


class LoginView(mixins.NoLoginRequired, generic.FormView):
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
        user = CustomUser.objects.create_user(phone=form.cleaned_data.get('phone'),
                                              password=form.cleaned_data.get('password'), )
        StudentProfile.objects.create(user_id=user.id)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class LogoutView(generic.View):
    def get(self, request):
        logout(self.request)
        return redirect(reverse('home:home'))


###################################################################

class UserProfileView(mixins.RequireSelfUser, generic.View):
    def get(self, request):
        return render(request, 'account/profile_table.html', {})


class UserEditProfileView(mixins.RequireSelfUser, generic.View):
    def get(self, request):
        if request.user.type == 'student':
            form = forms.UserEditForm(instance=request.user)
            form_student = forms.StudentProfileEditForm(instance=request.user.studentprofile)
            return render(request, 'account/profile_edit.html', {'form': form, 'form_student': form_student})
        elif request.user.type == 'consultant':
            form = forms.UserEditForm(instance=request.user)
            form_consultant = forms.ConsultantProfileEditForm(instance=request.user.consultantprofile)
            return render(request, 'account/profile_edit.html',
                          {'form': form, 'form_consultant': form_consultant})

    def post(self, request):
        form = forms.UserEditForm(data=self.request.POST, instance=request.user)
        if request.user.type == 'student':
            form_student = forms.StudentProfileEditForm(data=self.request.POST, instance=request.user.studentprofile)
            if form.is_valid() and form_student.is_valid():
                form.save()
                form_student.save()
                messages.success(request, 'اطلاعات شما با موفقیت ثبت شد')
                return render(self.request, 'account/profile_edit.html', {'form': form, 'form_student': form_student})

        form_consultant = forms.ConsultantProfileEditForm(data=self.request.POST,
                                                          instance=request.user.consultantprofile)
        if form.is_valid() and form_consultant.is_valid():
            if self.request.FILES.get('image'):
                consultant_profile = form_consultant.save(commit=False)
                consultant_profile.image = self.request.FILES['image']
            form.save()
            form_consultant.save()
            messages.success(request, 'اطلاعات شما با موفقیت ثبت شد')
        return render(self.request, 'account/profile_edit.html',
                      {'form': form, 'form_consultant': form_consultant})


class AddBlogView(mixins.RequireSelfUser, mixins.IsConsultant, generic.FormView):
    template_name = 'account/add_blog.html'
    form_class = BlogForm
    success_url = reverse_lazy('account:profile_add_blog')

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.author = self.request.user.consultantprofile
        blog.save()
        return super(AddBlogView, self).form_valid(form)
