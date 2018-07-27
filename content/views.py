from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import Content
from .forms import ContentCreateForm
# Create your views here.

def home_view(requset):
    return render(requset,"base.html")

def content_createview(requset):
    template_name='content/form.html'
    context={}
    return render(requset,template_name,context)

class ContentListView(ListView):
    def get_queryset(self):
        return Content.objects.all()

class ContentDetailView(DetailView):
    def get_queryset(self):
        return Content.objects.all()
        