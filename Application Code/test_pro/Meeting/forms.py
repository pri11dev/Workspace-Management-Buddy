from django import forms
from .models import meet,Venture,new,Project

class NewMeet(forms.ModelForm):
    class Meta:
        model=meet
        fields="__all__"

class NewVenture(forms.ModelForm):
    class Meta:
        model=Venture
        fields="__all__"

class NewNew(forms.ModelForm):
    class Meta:
        model=new
        fields="__all__"

class NewProject(forms.ModelForm):
    class Meta:
        model=Project
        fields=("name","member1","member2","member3","member4","member5","desc")