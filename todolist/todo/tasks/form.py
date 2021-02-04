from django import forms
from django.forms import ModelForm

from .models import *

class taskform(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add New Text...'}))
    class Meta:
        model=Task
        fields='__all__'