from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from courses.models import Course, Dean
from subjects.admin import SubjectInline


class CourseAdmin(ModelAdmin):
    inlines = (SubjectInline,)


admin.site.register(Course, CourseAdmin)
admin.site.register(Dean)
