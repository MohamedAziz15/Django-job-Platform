from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.text import slugify
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
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job, self).save(*args, **kwargs)  # Call the real save() method

    class Meta:
        ordering = ['-id']

class category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(max_length=30,null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class company(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField()
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class jobApply(models.Model):
    job = models.ForeignKey('job',related_name='Apply_job',on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/",help_text="please upload your latest resume")
    cover_letter = models.TextField(max_length=500,help_text="please write your")
    github_url = models.URLField(null=True,blank=True,help_text="please enter github profile url")
    linkedin_url = models.URLField(null=True,blank=True,help_text="please enter Linkedin profile url")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username



