from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from research.models import Research


class ResearchList(ListView):
    model = Research


class ResearchDetail(DetailView):
    model = Research
