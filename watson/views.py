# from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Watson


# Create your views here.
class WatsonList(ListView):
    template_name = "list.html"
    model = Watson


class WatsonDetail(DetailView):
    template_name = "detail.html"
    model = Watson


class WatsonCreate(CreateView):
    template_name = "create.html"
    model = Watson
    fields = ("title", "memo")
    success_url = reverse_lazy("list")
