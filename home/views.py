from django.views.generic import TemplateView

from research.models import Research


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def researches(self):
        return Research.objects.order_by('submitted').reverse().all()

