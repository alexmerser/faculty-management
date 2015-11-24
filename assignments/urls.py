from django.conf.urls import url

from assignments.views import AssignmentDetail, AssignmentsList

urlpatterns = [
    url(r'^$',
        AssignmentsList.as_view(),
        name='assignments_list'),
    url(r'^(?P<pk>\d+)/?$',
        AssignmentDetail.as_view(),
        name='assignment_detail'),
]