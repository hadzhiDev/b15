from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .models import News, Category


class NewsTemplateView(TemplateView):
    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_list"] = News.objects.all()
        context["title"] = "News"
        print(context)
        return context
    

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'