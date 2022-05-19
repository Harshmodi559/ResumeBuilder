from django.contrib import admin
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login', views.Login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.Logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    # templates link
    path('select_template/<int:id>', views.select_template, name='select_temp'),
    path('template1/<int:id>', views.template1, name='template1'),
    path('template2/<int:id>', views.template2, name='template2'),
    path('template3/<int:id>', views.template3, name='template3'),
    path('template4/<int:id>', views.template4, name='template4'),
    # path('check_info/<int:id>',views.check_info,name='check_info'),
    path('download/<int:id>', views.download, name="download"),
    # path('history/<int:id>',views.history,name="history"),
]