from django.conf.urls import url

from research.views import ResearchList, ResearchDetail

urlpatterns = [
    url(r'^$',
        ResearchList.as_view(),
        name='research_list'),
    url(r'^(?P<pk>\d+)/?$',
        ResearchDetail.as_view(),
        name='research_detail'),

]
