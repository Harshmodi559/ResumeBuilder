import email
from email.policy import default
from pyexpat import model
from django.db import models
# from django.forms import modelformset_factory
# Create your models here.


class userDetails(models.Model):
    uid = models.IntegerField(primary_key=True)
    # user_id=models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    about = models.CharField(max_length=250, default="", blank=True)

    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    linkedin = models.URLField(max_length=300)  # url1
    github = models.URLField(max_length=300)  # new
    address = models.CharField(max_length=50)

    master_year_from = models.IntegerField(blank=True)  # master_year
    master_year_to = models.IntegerField(blank=True)  # new
    master_degree = models.CharField(max_length=50, blank=True)
    university_name = models.CharField(max_length=100, blank=True)

    # new
    school_year_from = models.IntegerField(blank=True)
    school_year_to = models.IntegerField(blank=True)
    school_degree = models.CharField(max_length=50, blank=True)
    school_name = models.CharField(max_length=100, blank=True)
    #

    lang1 = models.CharField(max_length=30, blank=True)

   # new   Interest
    hobby1 = models.CharField(max_length=100, blank=True)
   #
    job_title = models.CharField(max_length=100, blank=True)  # company_post
    company_role = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    company_year_from = models.IntegerField(blank=True)  # company_year
    company_year_to = models.IntegerField(blank=True)  # new
    role = models.CharField(max_length=500, blank=True)


# new Projects
    project_title = models.CharField(max_length=500, blank=True)
    project_link = models.URLField(max_length=300, blank=True)
    project_tagline = models.CharField(max_length=500, blank=True)
#

    skill1 = models.CharField(max_length=100, blank=True)

    #

# new achievement
    achievement1 = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.first_name+self.last_name
