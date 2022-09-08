from django.contrib import admin
from . import models


class ContactUsAdmin(admin.ModelAdmin):
    models = models.ContactUs
    list_display = ('full_name', 'phone', 'subject')


admin.site.register(models.ContactUs, ContactUsAdmin)
