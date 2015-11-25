
from assignments.models import Assignment
from research.models import Research
from django.views.generic.base import TemplateView

from django import template
from django.contrib.auth.models import Group
register = template.Library()

@register.filter(name='has_group')


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def researches(self):
        return Research.objects.order_by('submitted').reverse().all()

    def assignments(self):
        return Assignment.objects.order_by('deadline').reverse().all()

    def has_group(user, group_name):
        group = Group.objects.get(name=group_name)
        return True if group in user.groups.all() else False
