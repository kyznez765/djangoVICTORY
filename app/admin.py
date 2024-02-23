from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tovar)

@admin.register(Cart)
class Admincart(admin.ModelAdmin):
    list_display = ('user', 'tovar', 'count', 'summa')