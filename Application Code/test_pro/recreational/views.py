from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from .models import Menu,events
from django.utils import timezone
from test_pro import settings
from . import forms
# Create your views here.

def index(request):
    return render(request,'recreational/test3.html',{'logged':settings.logged})

# def index(request):
#     return redirect('/re')

def cafe(request):
    ob=Menu.objects.filter(Day=timezone.now().weekday() )
    return render(request,'recreational/test6.html',{'vary':ob,'logged':settings.logged})
# def cafe(request):
#     return redirect('/re')

# def sport(request):
#     return redirect('/re')
def sport(request):
    return render(request,'test51.html',{'val':events.objects.all(),'logged':settings.logged})

@permission_required('Can add menu')
@login_required
def newMenu(request):
    if request.method == 'POST':
        meet_form = forms.FormMenu(data=request.POST)
        if meet_form.is_valid() :
            meet = meet_form.save()
            meet.save()
            return redirect('/re/cafe')
        else:
            print(meet_form.errors)
    else:
        meet_form = forms.FormMenu()
    return render(request,'plugMenu.html',
                          {'user_form':meet_form,
                           'val':'','logged':settings.logged}
                           )

@permission_required('Can add events')
@login_required
def newEvent(request):
    if request.method == 'POST':
        meet_form = forms.FormEvent(data=request.POST)
        if meet_form.is_valid() :
            meet = meet_form.save()
            meet.save()
            return redirect('/re/sport')
        else:
            print(meet_form.errors)
    else:
        meet_form = forms.FormEvent()
    return render(request,'plugEve.html',
                          {'user_form':meet_form,
                           'val':'','logged':settings.logged}
                           )

# def index(request):
#     print(timezone.now().date().weekday())
#     ob=Menu.objects.filter( Day=timezone.now().date().weekday())
#     return render(request,'recreational/index.html',{'var':ob})