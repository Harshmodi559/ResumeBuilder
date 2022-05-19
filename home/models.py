import email
from email.policy import default
from pyexpat import model
from django.db import models
# from django.forms import modelformset_factory
# Create your models here.


class userDetails(models.Model):
    uid = models.AutoField(primary_key=True)
    # user_id=models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    about = models.CharField(max_length=250, default="")

    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    linkedin = models.URLField(max_length=300)  # url1
    github = models.URLField(max_length=300)  # new
    address = models.CharField(max_length=50)

    master_year_from = models.IntegerField()  # master_year
    master_year_to = models.IntegerField()  # new
    master_degree = models.CharField(max_length=50)
    university_name = models.CharField(max_length=100)

    # new
    school_year_from = models.IntegerField()
    school_year_to = models.IntegerField()
    school_degree = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    #

    lang1 = models.CharField(max_length=30)
    lang2 = models.CharField(max_length=30)  # new

   # new   Interest
    hobby1 = models.CharField(max_length=100)
    hobby2 = models.CharField(max_length=100)
    hobby3 = models.CharField(max_length=100)

   #
    job_title = models.CharField(max_length=100)  # company_post
    company_role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_year_from = models.IntegerField()  # company_year
    company_year_to = models.IntegerField()  # new
    role = models.CharField(max_length=500)


# new Projects
    project_title = models.CharField(max_length=500)
    project_link = models.URLField(max_length=300)
    project_tagline = models.CharField(max_length=500)
#

    skill1 = models.CharField(max_length=100)
    # new
    skill2 = models.CharField(max_length=100)
    skill3 = models.CharField(max_length=100)
    skill4 = models.CharField(max_length=100)
    skill5 = models.CharField(max_length=100)
    #

# new achievement
    achievement1 = models.CharField(max_length=300)
    achievement2 = models.CharField(max_length=300)
#

    def __str__(self):
        return self.first_name+self.last_name
