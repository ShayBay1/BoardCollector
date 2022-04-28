from django.contrib import admin

# Register your models here.
from .models import Board, Tuning
admin.site.register(Board)
admin.site.register(Tuning)