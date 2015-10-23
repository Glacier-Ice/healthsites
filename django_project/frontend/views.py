# -*- coding: utf-8 -*-
import logging
LOG = logging.getLogger(__name__)

from django.views.generic import TemplateView
from django.conf import settings


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        *debug* toggles GoogleAnalytics support on the main page
        """

        context = super(MainView, self).get_context_data(**kwargs)
        context['debug'] = settings.DEBUG
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class HelpView(TemplateView):
    template_name = 'help.html'
