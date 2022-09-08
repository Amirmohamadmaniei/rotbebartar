from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from . import models
from .forms import UserCreationForm, UserChangeForm





class ConsultantProfile(admin.StackedInline):
    model = models.ConsultantProfile


class StudentProfile(admin.StackedInline):
    model = models.StudentProfile


class CustomUserAdmin(UserAdmin):
    class Meta:
        model = models.CustomUser

    form = UserChangeForm
    add_form = UserCreationForm
    model = models.CustomUser
    inlines = (ConsultantProfile, StudentProfile)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

    list_display = ('phone', 'get_full_name', 'type', 'is_admin')
    list_filter = ('is_admin', 'type', 'sex',)
    fieldsets = (
        ('اطلاعات کاربری', {'fields': ('phone', 'password')}),
        ('اطلاعات شخصی',
         {'fields': ('first_name', 'last_name', 'major_high_school', 'age', 'sex', 'ostan', 'city')}),
        ('مجوز ها', {'fields': ('type', 'is_admin', 'is_active', 'slug')}),
    )
    add_fieldsets = (
        ('اطلاعات کاربری', {'fields': ('phone', 'password1', 'password2')}),
        ('اطلاعات شخصی',
         {'fields': ('first_name', 'last_name', 'major_high_school', 'age', 'sex', 'ostan', 'city')}),
        ('مجوز ها', {'fields': ('type', 'is_admin', 'is_active', 'slug')}),
    )

    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('-created',)
    filter_horizontal = ()


class CommentAdmin(admin.ModelAdmin):
    models = models.Comment
    list_display = ('user', 'consultant', 'text', 'status')
    list_editable = ('status',)
    list_filter = ('status',)
    ordering = ('-created',)


admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
