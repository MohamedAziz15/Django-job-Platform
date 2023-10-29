from django.shortcuts import render
from .models import job


def job_list(request):
    all_jobs = job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': all_jobs})

# Create your views here.
