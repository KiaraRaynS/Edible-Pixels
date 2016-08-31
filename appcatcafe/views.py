from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'indexview.html'


# Drinks
class CatuccinoView(TemplateView):
    template_name = 'catuccinoview.html'
