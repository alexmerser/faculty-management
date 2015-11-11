from django.views.generic.list import ListView

from courses.models import Course


class CoursesList(ListView):
    model = Course

