from django.contrib import admin
from . import models

admin.site.site_header = 'Infoportal Administration'
admin.site.index_title = 'Infoportal Administration'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class PostAdmin(admin.ModelAdmin):
    list_display = ["forum", "title", "created", "author", "image", "body", "publish", "modified", "send_mail"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
