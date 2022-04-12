import email
from email.policy import default
from django.db import models
from django.forms import modelformset_factory
# Create your models here.

class Details(models.Model):
    uid = models.AutoField(primary_key=True)
    # uid = models.IntegerField(max_length=255)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    profession=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_number=models.IntegerField(max_length=10)
    url1=models.URLField(max_length=300)
    address=models.CharField(max_length=50)
    master_year=models.IntegerField()
    master_degree=models.CharField(max_length=50)
    university_name=models.CharField(max_length=100)
    lang1=models.CharField(max_length=30)
    about=models.CharField(max_length=250,default="")

    def __str__(self):
        return self.first_name





