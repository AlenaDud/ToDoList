from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin


class HomePageView(TemplateResponseMixin, View):
    """Return home page"""


    def get(self, request):
        pass
