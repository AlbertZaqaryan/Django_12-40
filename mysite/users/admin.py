from django.contrib import admin
from .models import Human
# Register your models here.

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname']
    list_display_links = ['id', 'fname']
    search_fields = ['fname', 'lname']