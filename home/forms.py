from django import forms

from home.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('__all__')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control w-75 mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control w-75 mb-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control w-75 mb-2'}),
            'subject': forms.TextInput(attrs={'class': 'form-control w-75 mb-2'}),
            'body': forms.Textarea(attrs={'class': 'form-control area mb-2'}),
        }