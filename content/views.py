from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import Content
# Create your views here.

def home_view(requset):
    return render(requset,"base.html")

class ContentListView(ListView):
    def get_queryset(self):
        return Content.objects.all()

class ContentDetailView(DetailView):
    def get_queryset(self):
        return Content.objects.all()
        