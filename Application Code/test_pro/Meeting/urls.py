from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^meet/$',views.meet),
    url(r'^ven/$',views.vent),
    url(r'^new/$',views.new),
    url(r'^meet/newmeet/$',views.meetNew),
    url(r'^new/newnew/$',views.newNew),
    url(r'^ven/newven/$',views.venNew),
    url(r'^bot/',views.bot),
    url(r'^ven/pro',views.pro),
    url(r'^ven/guide',views.gui),
    url(r'^guide/back',views.back),
    url(r'^guide/front',views.front),
    
    
]
