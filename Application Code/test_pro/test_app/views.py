from django.shortcuts import render,redirect
from test_app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from test_pro import settings

from . import views as vv

client=0

def index(request):
    return render(request,'dell (1).html',{'logged':settings.logged})

# def index(request):
#     return render(request,'new_project_description.html',{'logged':settings.logged})

def index1(request):
    return render(request,'dell2n.html',{'logged':settings.logged})
def index2(request):
    return render(request,'test1.html',{'logged':settings.logged})

@login_required
def special(request):
    return HttpResponse("You are logged in !",{'logged':settings.logged})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_logout(request):
    logout(request)
    global client
    vv.client=0
    settings.logged=False
    User.is_authenticated=False
    # print("##################")
    # v=User.is_authenticated
    # print(v)
    return render(request,'dell (1).html',{'logged':False})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        st=request.POST['email'].split('@')[1]    
        st1=st.split('.')[0]
        if user_form.is_valid() and profile_form.is_valid() and st1=="dell":
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('/home/user_login')
        elif st1!="dell":
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
            return render(request,'test_app/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'val':"Please Enter an Email with dell.com/.in....",'logged':settings.logged})
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    if settings.logged:
        return redirect('/next1')
    else:
        print("#########")
        print(settings.logged)
        return render(request,'test_app/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':settings.logged,'logged':settings.logged})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                settings.logged=True
                return redirect('/next1')
                # return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login_form.html',{'logged':settings.logged})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'login_form.html', {'val':"Username and Password didn't match!!!!"})
    else:
        if settings.logged:
            return redirect('/next1')
        return render(request, 'login_form.html',{'logged':settings.logged})