from django.contrib import admin
from .models import Student, Book, Rental
# Register your models here.

admin.site.register(Student)
admin.site.register(Rental)