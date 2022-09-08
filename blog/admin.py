from django.contrib import admin
from . import models


class BlogAdmin(admin.ModelAdmin):
    models = models.Blog
    list_display = ('author', 'title', 'status')
    list_editable = ('status',)
    list_filter = ('author', 'status',)
    ordering = ('-created',)


admin.site.register(models.Blog, BlogAdmin)
