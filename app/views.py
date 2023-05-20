from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView

# Create your views here.

class home(TemplateView):
    template_name='app/home.html'

class school_list(ListView):
    model=School
    context_object_name='schools'

class school_detail(DetailView):
    model=School
    context_object_name='sclobject'
