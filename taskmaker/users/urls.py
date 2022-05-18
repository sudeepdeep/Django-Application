from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.users),
    path('createteam/', views.createteam),
    path('createtask/', views.createtask),
    path('lead/', views.taskstolead),
    path('member/', views.tasktomember),
    path('alltasks/', views.alltasks),
    re_path(r'^update/(?P<task>\w{0,50})/$', views.updatestatus),
]