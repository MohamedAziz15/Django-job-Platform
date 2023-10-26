from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here.

jobType = (
    ('full time', 'full time'),
    ('part time', 'part time'),
    ('remote', 'remote'),
    ('freelance', 'freelance')
)


class job(models.Model):
    title = models.CharField(max_length=120)
    Location = CountryField()
    company = models.ForeignKey(
        'company', on_delete=models.CASCADE, related_name='job_company')
    created_at = models.DateTimeField(default=timezone.now)
    salary_start = models.IntegerField(null=True, blank=True)
    salary_end = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=15000)
    vacancy = models.IntegerField()
    job_type = models.CharField(choices=jobType, max_length=10)
    experience = models.IntegerField()
    category = models.ForeignKey(
        'category', on_delete=models.SET_NULL, related_name='job_category', null=True, blank=True)


class category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(max_length=30)


class company(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField()
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()
