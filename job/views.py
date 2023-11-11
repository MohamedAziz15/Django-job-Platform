from django.shortcuts import render
from .models import job

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def job_list(request):
    #all_jobs = job.objects.all().order_by('-id')
    all_jobs = job.objects.all()
    jobs_count = all_jobs.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 10)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)

    return render(request, 'job/job_list.html', {'jobs': all_jobs},{'jobs_count':jobs_count})

def job_detail(request, slug):
    Job = job.objects.get(slug=slug)
    return render(request, 'job/job_detail.html', {'job': Job})
# Create your views here.
