# Generated by Django 4.0.4 on 2022-05-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_userdetails_achievement2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='about',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='achievement1',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_role',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_year_from',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='company_year_to',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='hobby1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='job_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='lang1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='master_degree',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='master_year_from',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='master_year_to',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='project_link',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='project_tagline',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='project_title',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='role',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='school_degree',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='school_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='school_year_from',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='school_year_to',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='skill1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='university_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]