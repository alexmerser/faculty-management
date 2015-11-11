from django.conf.urls import url

from courses.views import CoursesList

urlpatterns = [
    url(r'^$',
        CoursesList.as_view(),
        name='courses_list'),
]
