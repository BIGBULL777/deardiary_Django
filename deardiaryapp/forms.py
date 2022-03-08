from .models import *
from django import forms
from django.forms import ModelForm


class EntryForm(forms.ModelForm):
    class Meta():
        model = Diary
        fields = '__all__'

        