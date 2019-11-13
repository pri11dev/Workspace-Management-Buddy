from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse
from . import views
from . import models
from test_pro import settings
from . import forms
from django.contrib.auth.models import User
from test_app import models as m



# Create your views here.
@login_required
def index(request):
    return render(request,'test2.html',{'logged':settings.logged})

@login_required
def meet(request):
    return render(request,'test5.html',{'val':models.meet.objects.all(),'logged':settings.logged})


@login_required
def vent(request):
    return render(request,'test4.html',{'i':models.Venture.objects.all(),'logged':settings.logged})

@login_required
def new(request):
    return render(request,'what.html',{'val':models.new.objects.all(),'logged':settings.logged})

@login_required
def pro(request):
    return render(request,'new_project_description.html',{'val':models.Project.objects.all(),'logged':settings.logged})


@permission_required('Can add meet')
@login_required
def meetNew(request):
    if request.method == 'POST':
        meet_form = forms.NewMeet(data=request.POST)
        if meet_form.is_valid() :
            meet = meet_form.save()
            meet.save()
            return redirect('/meeting/meet')
        else:
            print(meet_form.errors)
    else:
        meet_form = forms.NewMeet()
    return render(request,'plugMeet.html',
                          {'user_form':meet_form,
                           'val':'','logged':settings.logged}
                           )

@permission_required('Can add venture')
@login_required
def venNew(request):
    if request.method == 'POST':
        meet_form = forms.NewVenture(data=request.POST)
        if meet_form.is_valid() :
            meet = meet_form.save()
            meet.save()
            return redirect('/meeting/ven')
        else:
            print(meet_form.errors)
    else:
        meet_form = forms.NewVenture()
    return render(request,'plugVen.html',
                          {'user_form':meet_form,
                           'val':'','logged':settings.logged}
                           )

@permission_required('Can add new')
@login_required
def newNew(request):
    if request.method == 'POST':
        meet_form = forms.NewNew(data=request.POST)
        if meet_form.is_valid() :
            meet = meet_form.save()
            meet.save()
            return redirect('/meeting/new')
        else:
            print(meet_form.errors)
    else:
        meet_form = forms.NewNew()
    return render(request,'plugNew.html',
                          {'user_form':meet_form,
                           'val':'','logged':settings.logged}
                           )
@login_required
def bot(request):
    return render(request,'bot.html',{'logged':settings.logged})

@login_required
def pro(request):
    return render(request,'new_project_description.html',{'logged':settings.logged,'val':models.Project.objects.all()})

@login_required
def gui(request):
    return render(request,'test10.html',{'logged':settings.logged})

@login_required
def back(request):
    return render(request,'index_back_guide.html',{'logged':settings.logged,})


@login_required
def front(request):
    return render(request,'index_front_guide.html',{'logged':settings.logged,})