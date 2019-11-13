from django import forms
from . import models

class FormMenu(forms.ModelForm):
    class Meta:
        model=models.Menu
        fields="__all__"

class FormEvent(forms.ModelForm):
    class Meta:
        model=models.events
        fields="__all__"
