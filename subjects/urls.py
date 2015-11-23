from django.conf.urls import url

from subjects.views import SubjectList, SubjectDetail

urlpatterns = [
    url(r'^byCourse/(?P<pk>\d+)$',
        SubjectList.as_view(),
        name='subject_list'),
    url(r'^(?P<pk>\d+)/?$',
        SubjectDetail.as_view(),
        name='subject_detail'),
]
