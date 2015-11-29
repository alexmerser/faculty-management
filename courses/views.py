from django.views.generic import DetailView
from django.views.generic.list import ListView

from courses.models import Course
from exams.models import Grade


class CoursesList(ListView):
    model = Course


class CourseDetail(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subjects = []
        for subject in self.object.subject_set.all():
            students = []
            exams = subject.exam_set.order_by('date')
            for student in self.object.student_set.all():
                grades = []
                for exam in exams:
                    try:
                        grade = Grade.objects.get(student=student, exam=exam)
                    except Grade.DoesNotExist:
                        grade = None
                    grades.append(grade)
                students.append(dict(
                    obj=student,
                    grades=grades,
                ))
            subjects.append(dict(
                pk=subject.pk,
                name=subject.name,
                exams=exams,
                staff = subject.staff,
                students=students,
            ))
        context['subjects'] = subjects
        return context
