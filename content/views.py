from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Content
from .forms import ContentCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home_view(requset):
    return render(requset,"registration/login.html")

class ContentCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class= ContentCreateForm
    template_name='content/form.html'
    success_url='/muvi/'

    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        return super(ContentCreateView,self).form_valid(form)
   


class ContentListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    def get_queryset(self):
        return Content.objects.filter(owner=self.request.user)

    

class ContentUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    form_class=ContentCreateForm
    template_name='content/detail-update.html'
    success_url='/muvi/'
    def get_queryset(self):
        return Content.objects.filter(owner=self.request.user)

    def get_context_data(self,*args,**kwargs):
        context=super(ContentUpdateView,self).get_context_data(*args,**kwargs)
        name=self.get_object().name
        context['title']=f'Update Restaurants:{name}'
        return context

class ContentDeleteView(LoginRequiredMixin,DeleteView):
    model=Content
    success_url='/muvi/'
