from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View, TemplateView


class HomePageView(View):
    """Return home page"""
    template_name = 'lists/home.html'

    def get(self, request):
        return render(request, 'lists/home.html')
