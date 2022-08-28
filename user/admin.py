from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from . import models
from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm


class ConsultantProfile(admin.TabularInline):
    model = models.Profile


class CustomUserAdmin(UserAdmin):
    class Meta:
        model = models.CustomUser

    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser
    inlines = (ConsultantProfile,)

    list_display = ('phone', 'type', 'is_admin')
    list_filter = ('is_admin', 'type')
    fieldsets = (
        ('اطلاعات کاربری', {'fields': ('phone', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'major', 'age', 'sex')}),
        ('مجوز ها', {'fields': ('type', 'consultant', 'is_admin', 'is_active')}),
    )
    add_fieldsets = (
        ('اطلاعات کاربری', {'fields': ('phone', 'password1', 'password2')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'major', 'age', 'sex')}),
        ('مجوز ها', {'fields': ('type', 'consultant', 'is_admin', 'is_active')}),
    )

    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
