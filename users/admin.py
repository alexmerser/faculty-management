from django.contrib import admin

from users.models import Student, Staff

admin.site.register(Student)
admin.site.register(Staff)
