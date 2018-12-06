from django.contrib import admin

# Register your models here.

from.models import Board,Picture,localUsers

admin.site.register(Board)
admin.site.register(Picture)
admin.site.register(localUsers)