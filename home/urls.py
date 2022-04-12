from django import views
from django.urls import path
from . import views

urlpatterns = [
 path('',views.home,name="home"),

 path('login',views.Login,name="login"),
 path('signup',views.signup,name="signup"),
 path('signout',views.signout,name="signout"),
 path('dashboard',views.dashboard,name="dashboard"),
#### templates link
# path('template1',views.template1,name='template1'),
path('template1/<int:id>',views.template1,name='template1'),
# path('check_info/<int:id>',views.check_info,name='check_info'),

]


#  path('templates',views.select_template,name="select_template"),
#  path('create',views.create_resume,name="create_resume"),
#  path('view',views.view,name="view"),
#  path('download',views.download,name="download"),