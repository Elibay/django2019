from django.contrib import admin

# Register your models here.
from api.models import Student, Class

admin.site.register(Student)
admin.site.register(Class)