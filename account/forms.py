from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from account.validations import start_with_09, is_digit
from user.models import CustomUser, ConsultantProfile, StudentProfile
from home import information


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
        return phone


####################################################################################

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ('is_admin', 'is_active', 'password', 'type', 'consultant', 'created', 'last_login')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ostan': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}, choices=information.sex_type),
            'major_high_school': forms.Select(attrs={'class': 'form-control'}, choices=information.major_high_schools),
        }


class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('grade',)
        widgets = {
            'grade': forms.Select(attrs={'class': 'form-control'}, choices=information.grades),
        }


class ConsultantProfileEditForm(forms.ModelForm):
    class Meta:
        model = ConsultantProfile
        fields = ('description', 'university', 'major_university', 'image', 'capacity', 'tel')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'major_university': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
        }
