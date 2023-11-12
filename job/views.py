from django.shortcuts import render
from .models import job, jobApply
from django.views.generic import CreateView 
from django.shortcuts import get_object_or_404
from .form import jobApplyForm, AddjobForm


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



class jobApply(CreateView):
    model = jobApply
    success_url = '/jobs/'
    #fields = ['username', 'email', 'resume', 'cover_letter', 'github_url', 'linkedin_url']
    form_class = jobApplyForm

    def form_valid(self, form):
        # Extract the slug from the URL
        slug = self.kwargs['slug']

        # Get the job object based on the slug
        #get_object_or_404: doesn't cause any crashes if system didn't contain this [slug]
        job_ = get_object_or_404(job, slug=slug)

        # Create a new jobApply object and set the job and form data
        apply_job = form.save(commit=False)
        apply_job.job = job_

        # Save the jobApply object
        apply_job.save()

        return super().form_valid(form)




class addJob(CreateView):
    model = job
    success_url = '/jobs/'
    # fields = ['title', 'Location', 'company', 'salary_start', 'salary_end', 'description','vacancy','job_type','experience','category']
    form_class = AddjobForm

