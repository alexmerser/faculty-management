from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from exams.models import Exam, ExamType, Grade


class GradeInline(TabularInline):
    model = Grade
    fields = ('student', 'exam', 'value',)


class ExamAdmin(ModelAdmin):
    inlines = (GradeInline,)


admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamType)
admin.site.register(Grade)
