from django import forms
from . models import Taskmodel

class TaskMod(forms.ModelForm):
    class Meta:
        model=Taskmodel
        fields= '__all__'