from pydoc import render_doc
from tempfile import template
from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from home.models import userDetails
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
# for pdf download
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit
from xhtml2pdf import pisa
import os


def home(request):
    return render(request, 'home.html')


def entries(request, id):
    if(request.method == "POST"):
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        profession = request.POST.get('profession')
        about = request.POST.get('about')
        # contact info
        email = request.POST.get('email')
        ph_no = request.POST.get('phone_number')
        github_link = request.POST.get('github')
        address = request.POST.get('address')
        linkedin_link = request.POST.get('linkedin')
      # education
        # address linkedin master_year master_degree university_name lang1 company_year company_post
        master_year_from = request.POST.get('master_year_from')
        master_year_to = request.POST.get('master_year_to')
        master_degree = request.POST.get('master_degree')
        university_name = request.POST.get('university_name')

        school_degree = request.POST.get('school_degree')
        school_year_to = request.POST.get('school_year_to')
        school_year_from = request.POST.get('school_year_from')
        school_name = request.POST.get('school_name')
# language

        lang1 = request.POST.get('language1')
        # lang2 = request.POST.get('language2')
        # 3 hobby
        hobby1 = request.POST.get('hobby1')
        # hobby2 = request.POST.get('hobby2')
        # hobby3 = request.POST.get('hobby3')

# experience
        company_year_from = request.POST.get('company_year_from')
        company_year_to = request.POST.get('company_year_from')
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        company_role = request.POST.get('company_role')
        role = request.POST.get('role')

    # projects
        project_title = request.POST.get('project_title')
        project_link = request.POST.get('project_link')
        project_tagline = request.POST.get('project_tagline')

# skills
        skill1 = request.POST.get('skill1')
        # skill2 = request.POST.get('skill2')
        # skill3 = request.POST.get('skill3')
        # skill4 = request.POST.get('skill4')
        # skill5 = request.POST.get('skill5')
# achievement
        achievement1 = request.POST.get('achievement1')
        # achievement2 = request.POST.get('achievement2')
    ##############

        if(fname != '' and lname != '' and profession != '' and about != '' and email != '' and ph_no != '' and github_link != '' and address != '' and linkedin_link != '' and
           master_year_from != '' and master_degree != '' and university_name != '' and
           master_year_to != '' and school_year_from != '' and school_year_to != '' and
           school_degree != '' and school_name != '' and lang1 != '' and hobby1 != ''
           and company_year_from != '' and company_year_to != ''
           and job_title != '' and company_name != '' and company_role != '' and role != ''
           and project_title != '' and project_link != '' and project_tagline != '' and
           skill1 != '' and
           achievement1 != ''):
            print("data has camed !!!!")
            try:

                Details = userDetails(uid=id, first_name=fname, last_name=lname, profession=profession, about=about,
                                      email=email, phone_number=ph_no, github=github_link, linkedin=linkedin_link, address=address,
                                      master_year_from=master_year_from, master_year_to=master_year_to, master_degree=master_degree, university_name=university_name,
                                      skill1=skill1,
                                      school_degree=school_degree, school_name=school_name, school_year_from=school_year_from, school_year_to=school_year_to,
                                      lang1=lang1,
                                      hobby1=hobby1,
                                      achievement1=achievement1,
                                      project_title=project_title, project_tagline=project_tagline, project_link=project_link,
                                      job_title=job_title, company_name=company_name, company_role=company_role, company_year_from=company_year_from, company_year_to=company_year_to, role=role
                                      )
                Details.save()
                messages.success(request, 'Saved to DB')
                # print(Details.uid)
                return redirect('/select_template/{}'.format(Details.uid))

            # else:
            #     messages.warning(request, "Already Exist")
            except Exception as e:
                print(e)
                messages.warning(
                    request, "Something went wrong! Please provide proper data")
    return render(request, 'entries.html')


def Login(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = User.objects.get(username=username)
        # print(user)
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, "Login Successfully!!")
            login(request, user)
            # print(user.id)
            # print(type(user.id))
            # request.session['isLogged']=True
            # request.session['person_id']=user.id

            return redirect('dashboard/{}'.format(user.id))
    return redirect('home')


def signup(request):
    if(request.method == "POST"):
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        newUser = User.objects.create_user(username, user_email, user_password)
        newUser.first_name = fname
        newUser.save()
        messages.success(request, "Account Created Successfully !!")
    return redirect('home')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logout")
    return redirect('/')


# template
def select_template(request, id):
    data = userDetails.objects.get(uid=id)
    if(data == ''):
        return HttpResponse("<h1>NOT FOUND<h1>")
    else:
        return render(request, "select_temp.html", {'id': id})


def remove(string):
    return "".join(string.split())


def create_list(string):
    x = remove(string)
    list = []
    a = ''
    for i in x:
        if(i == ','):
            if(a != ''):
                list.append(a)
            a = ''
        else:
            a = a+i
    list.append(a)
    return list


def template1(request, id):
    data = userDetails.objects.get(uid=id)
    hobby_list = create_list(data.hobby1)
    achievement_list = create_list(data.achievement1)
    lang_list = create_list(data.lang1)
    skill_list = create_list(data.skill1)
    # print(data.first_name)
    # print("////")
    return render(request, "resume_templates/first_temp.html", {'data': data, 'hobby': hobby_list, 'achievement': achievement_list, 'skill': skill_list, 'lang': lang_list})


def template2(request, id):
    data = userDetails.objects.get(uid=id)
    # interest
    # interest_string=data.hobby1
    hobby_list = create_list(data.hobby1)
    achievement_list = create_list(data.achievement1)
    lang_list = create_list(data.lang1)
    skill_list = create_list(data.skill1)
    # print(data.first_name)
    return render(request, "resume_templates/temp2.html", {'data': data, 'hobby': hobby_list, 'achievement': achievement_list, 'skill': skill_list, 'lang': lang_list})


def template3(request, id):
    data = userDetails.objects.get(uid=id)
    hobby_list = create_list(data.hobby1)
    achievement_list = create_list(data.achievement1)
    lang_list = create_list(data.lang1)
    skill_list = create_list(data.skill1)
    # print(data.first_name)
    return render(request, "resume_templates/temp3.html", {'data': data, 'hobby': hobby_list, 'achievement': achievement_list, 'skill': skill_list, 'lang': lang_list})


def template4(request, id):
    data = userDetails.objects.get(uid=id)
    hobby_list = create_list(data.hobby1)
    achievement_list = create_list(data.achievement1)
    lang_list = create_list(data.lang1)
    skill_list = create_list(data.skill1)
    # print(data.first_name)
    return render(request, "resume_templates/temp4.html", {'data': data, 'hobby': hobby_list, 'achievement': achievement_list, 'skill': skill_list, 'lang': lang_list})


# download pdf

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None


def download(request, id):
    data = userDetails.objects.get(uid=id)
    dic = {'dict': data}
    pdf = render_to_pdf('resume_templates/first_temp.html', dic)
    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        filename = "Resume_%s.pdf" % (data.first_name)
        content = "inline; filename='%s'" % (filename)
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not Found")


# def history(request,id):
#     data=userDetails.objects.(pk=id)
#     print("////////////")
#     print(len(data))
#     return render(request,"history.html",{'data':data})
    # prnt
# def list(request):
#     profile = userDetails.objects.all()
#     return render(request, "list.html", {'list': profile})


def dashboard(request, id):
    # print(type(id))
    return render(request, "dashboard.html", {'id': id})
