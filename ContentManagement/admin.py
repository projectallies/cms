from django.contrib import admin
from ContentManagement.models import Pages

class PagesAdmin(admin.ModelAdmin):
    list_display = ('Title',)
# Register your models here.
admin.site.register(Pages)
