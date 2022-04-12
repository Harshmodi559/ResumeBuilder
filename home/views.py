from pydoc import render_doc
from tempfile import template
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login ,logout
from .models import Details

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

def home(request):
    return render(request,'home.html')


def dashboard(request):
    return render(request,'dashboard.html')


def Login(request):
    if(request.method=="POST"):
        username=request.POST['name']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return redirect('dashboard')
    return  redirect('home')       

def signup(request):
    if(request.method=="POST"):
      fname=request.POST['fname']  
      username=request.POST['username']
      user_email=request.POST['email']
      user_password=request.POST['password']
      user_password2=request.POST['password2']
      newUser=User.objects.create_user(username,user_email,user_password)
      newUser.first_name=fname
      newUser.save()
    #   messages.success(request,"Account Created Successfully !!")
    return redirect('home')    

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required(login_url='login')
def signout(request):
    logout(request)
    # messages(request,"Successfully logout")
    return redirect('home')

def template1(request,id):
    if(request.method=="POST"):
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        profession=request.POST['profession']
        email=request.POST['email']
        ph_no=request.POST['phone_number']
        web_link=request.POST['website_link']
        address=request.POST['address']
        master_year=request.POST['master_year']
        master_degree=request.POST['master_degree']
        university_name=request.POST['university_name']
        lang1=request.POST['language1']
        about=request.POST['about']
       
        b=Details(uid=id,first_name=fname,last_name=lname,profession=profession,email=email,
        phone_number=ph_no,url1=web_link,address=address,master_year=master_year,master_degree=master_degree,
        university_name=university_name,lang1=lang1,about=about)
        b.save()

        # user_id=Details.objects.get(id=id) 
    # all_data= Details.objects.all()
    # print(all_data)
    # filter_results = all_data.filter(uid=id)
    # print(id)
    data=Details.objects.get(pk=id)
    dict={'first_name':data.first_name,'last_name':data.last_name,'profession':data.profession,'email':data.email,'phone_number':data.phone_number,
    'url1':data.url1,'address':data.address,'master_year':data.master_year,'lang1':data.lang1,'about':data.about}
    # print(data)
    # list(data.objects.all())
    print("heheeh")
    # print(context['results'])
    return render(request,"resume_templates/first_temp.html",{'dict':dict})


def check_info(request,id):
    pass