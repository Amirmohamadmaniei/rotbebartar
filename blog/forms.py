from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            # 'tag': forms.CharField(attrs='form-control'),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        blog = Blog.objects.filter(title=title).exists()
        if blog == True:
            raise ValidationError('مقاله ای با این عنوان از قبل موجود است')

        return title
