from django.contrib import admin
from django.contrib.admin.options import TabularInline

from subjects.models import Subject


class SubjectInline(TabularInline):
    model = Subject
    fields = ('course', 'name')


admin.site.register(Subject)
