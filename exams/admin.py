from django.contrib import admin

from exams.models import Exam, ExamType, Grade

admin.site.register(Exam)
admin.site.register(ExamType)
admin.site.register(Grade)

