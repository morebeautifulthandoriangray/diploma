from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document
from pydocx import PyDocX
from .models import Document, Sample

# Create your views here.


class DocumentListView(ListView):
    model = Document
    template_name = 'documents_all.html'


class SampleListView(ListView):
    model = Sample
    template_name = 'samples_list.html'


class SampleDetailView(DetailView):
    model = Sample
    template_name = 'sample_detail.html'


class SampleCreateView(CreateView):
    model = Sample
    template_name = 'sample_new.html'
    fields = ['title', 'path_to_template']


class SampleUpdateView(UpdateView):
    model = Sample
    template_name = 'sample_edit.html'
    fields = ['title', 'path_to_template']


class SampleDeleteView(DeleteView):
    model = Sample
    template_name = 'sample_delete.html'
    success_url = reverse_lazy('samples_all')