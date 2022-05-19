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


def dashboard(request):
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
        lang2 = request.POST.get('language2')
        # 3 hobby
        hobby1 = request.POST.get('hobby1')
        hobby2 = request.POST.get('hobby2')
        hobby3 = request.POST.get('hobby3')

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
        skill2 = request.POST.get('skill2')
        skill3 = request.POST.get('skill3')
        skill4 = request.POST.get('skill4')
        skill5 = request.POST.get('skill5')
# achievement
        achievement1 = request.POST.get('achievement1')
        achievement2 = request.POST.get('achievement2')
    ##############

        if(fname and lname and profession and about and email and ph_no and github_link and address and linkedin_link and master_year_from and master_degree and university_name and master_year_to and school_year_from and school_year_to and school_degree and school_name and lang1 and lang2 and hobby1 and hobby2 and hobby3 and company_year_from and company_year_to and job_title and company_name and company_role and role and project_title and project_link and project_tagline and skill1 and skill2 and skill3 and skill4 and skill5 and achievement1 and achievement2):
            print("data has camed !!!!")
            try:
                d = userDetails.objects.filter(phone_number=ph_no, first_name=fname)

                print(len(d))

                if(len(d) == 0):
                    Details = userDetails(first_name=fname, last_name=lname, profession=profession, about=about,
                                          email=email, phone_number=ph_no, github_link=github_link, linkedin=linkedin_link, address=address,
                                          master_year_from=master_year_from, master_year_to=master_year_to, master_degree=master_degree, university_name=university_name,
                                          skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, skill5=skill5,
                                          school_degree=school_degree, school_name=school_name, school_year_from=school_year_from, school_year_to=school_year_to,
                                          lang1=lang1, lang2=lang2,
                                          hobby1=hobby1, hobby2=hobby2, hobby3=hobby3,
                                          achievement1=achievement1, achievement2=achievement2,
                                          project_title=project_title, project_tagline=project_tagline, project_link=project_link,
                                          job_title=job_title, company_name=company_name, company_role=company_role, company_year_from=company_year_from, company_year_to=company_year_to, role=role
                                          )
                    Details.save()
                    messages.success(request, 'Saved to DB')
                    print(Details.uid)
                    # print(type(Details.uid))
                    return redirect('/select_template/{}'.format(Details.uid))
                    # if(id==1):
                    #     return redirect('/template1/{}'.format(Details.uid))

                    # elif(id==2):
                    #     return redirect('/template2/{}'.format(Details.uid))

                    # elif(id==3):
                    #     return redirect('/template3/{}'.format(Details.uid))

                    # elif(id==4):
                    #     return redirect('/template4/{}'.format(Details.uid))

                else:
                    messages.warning(request, "Already Exist")
            except Exception as e:
                print(e)
    return render(request, 'dashboard.html')


def Login(request):
    if(request.method == "POST"):
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        # print(user)
        if user is not None:
            messages.success(request, "Login Successfully!!")
            login(request, user)

            # request.session['isLogged']=True
            # request.session['person_id']=user.id

            return redirect('dashboard')
    return redirect('home')


def signup(request):
    if(request.method == "POST"):
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_password2 = request.POST.get('password2')
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
    return render(request, "select_temp.html", {'id': id})


def template1(request, id):
    data = userDetails.objects.get(uid=id)
    return render(request, "resume_templates/first_temp.html", {'d': data})


def template2(request, id):
    data = userDetails.objects.get(uid=id)
    return render(request, "resume_templates/temp2.html", {'d': data})


def template3(request, id):
    data = userDetails.objects.get(uid=id)
    return render(request, "resume_templates/temp3.html", {'d': data})


def template4(request, id):
    data = userDetails.objects.get(uid=id)
    return render(request, "resume_templates/temp4.html", {'d': data})


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
