from django.conf.urls import url

from courses.views import CoursesList, CourseDetail

urlpatterns = [
    url(r'^(?P<pk>\d+)/?$',
        CourseDetail.as_view(),
        name='course_detail'),
    url(r'^$',
        CoursesList.as_view(),
        name='courses_list'),
]
