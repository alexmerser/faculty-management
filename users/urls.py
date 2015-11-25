from django.conf.urls import url

from users.views import StudentsDetail, StaffsDetail, DeansDetail

urlpatterns = [
    url(r'^$',
        StudentsDetail.as_view(),
        name='student_list'),
    url(r'^(?P<pk>\d+)/?$',
        StaffsDetail.as_view(),
        name='staff_detail'),
    url(r'^$',
        DeansDetail.as_view(),
        name='dean_list'),
]
