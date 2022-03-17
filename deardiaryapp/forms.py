from .models import *
from django import forms
from django.forms import ModelForm,widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EntryForm(forms.ModelForm):
    class Meta():
        model = Diary
        fields = '__all__'
        widget = {
            'Entry':forms.TextInput(attrs={'class':'form-control'}),
        }

        

# class User_creation(forms.ModelForm):
#     class Meta():
#         model = User
#         fields = ['username','password1','password2']