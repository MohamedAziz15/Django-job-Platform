from django.shortcuts import render
from .models import job


def job_list(request):
    #all_jobs = job.objects.all().order_by('-id')
    all_jobs = job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': all_jobs})

def job_detail(request, slug):
    Job = job.objects.get(slug=slug)
    return render(request, 'job/job_detail.html', {'job': Job})
# Create your views here.
