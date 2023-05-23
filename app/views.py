from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class home(TemplateView):
    template_name='app/home.html'

class school_list(ListView):
    model=School
    context_object_name='schools'

class school_detail(DetailView):
    model=School
    context_object_name='sclobject'

class school_create(CreateView):
    model=School
    fields='__all__'

class school_update(UpdateView):
    model=School
    fields='__all__'

class school_delete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('school_list')
