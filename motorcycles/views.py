from urllib import request

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView, CreateView

from motorcycles.forms import Addmotorcycleform


class Add(CreateView):
    template_name = 'motorcycles/add.html'
    form_class = Addmotorcycleform

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
