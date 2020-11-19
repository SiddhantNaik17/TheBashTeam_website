from django import forms
from django.urls import reverse

from motorcycles.models import Motorcycle


class Addmotorcycleform(forms.ModelForm):
    name = forms.CharField(required=True)
    manufacture = forms.CharField(required=True)

    class Meta:
        model = Motorcycle
        fields = '__all__'
