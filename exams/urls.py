from django.conf.urls import url

from exams.views import ExamsList, ExamDetail

urlpatterns = [
    url(r'^$',
        ExamsList.as_view(),
        name='exams_list'),
    url(r'^(?P<pk>\d+)/?$',
        ExamDetail.as_view(),
        name='exam_detail'),
    ]
