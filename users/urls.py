from django.conf.urls import url

from users.views import StudentsList, StaffsList, DeansList

urlpatterns = [
    url(r'^$',
        StudentsList.as_view(),
        name='student_list'),
    url(r'^(?P<pk>\d+)/?$',
        StaffsList.as_view(),
        name='staff_list'),
    url(r'^$',
        DeansList.as_view(),
        name='dean_list'),
]