from django import forms
from django.contrib.auth import authenticate
from django.core import validators
from django.core.exceptions import ValidationError

from account.validations import start_with_09, is_digit
from user.models import CustomUser


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'شماره تلفن'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'رمز عبور'}))

    def clean(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        user = authenticate(phone=phone, password=password)
        if user is None:
            raise ValidationError('شماره تلفن یا رمز عبور اشتباه است لطفا دوباره امتحان کنید')


class RegisterForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'شماره تلفن'}),
        validators=[start_with_09, is_digit])
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'تکرار رمز عبور'}))

    def clean(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        user = CustomUser.objects.filter(phone=phone).exists()
        if user:
            raise ValidationError('شماره تلفن از قبل وجود دارد')

        if password != password2:
            raise ValidationError('کلمه های عبور یکسان نیست')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) > 11 or len(phone) < 11:
            raise ValidationError('شماره تلفن باید 11 رقمی باشد')
