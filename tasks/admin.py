from django.contrib import admin
from .models import *     #to import all models, can import individually too
# Register your models here.
admin.site.register(Task)