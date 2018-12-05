from django.contrib import admin

# Register your models here.

from.models import Board
from .models import Picture

admin.site.register(Board)
admin.site.register(Picture)