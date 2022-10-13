from django.contrib import admin
from .models import Menutext
# Register your models here.

class MenuTextAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

admin.site.register(Menutext, MenuTextAdmin)