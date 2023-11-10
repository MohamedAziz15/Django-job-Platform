from django.contrib import admin
from .models import category, company, job
from django_summernote.admin import SummernoteModelAdmin




class jobadmin(SummernoteModelAdmin):
    list_display = ['title', 'company', 'Location',
                    'vacancy', 'job_type', 'category']
    search_fields = ('title', 'category', 'description')
    list_filter = ('vacancy', 'job_type', 'category', 'experience')
    summernote_fields = '__all__'



admin.site.register(job, jobadmin)
admin.site.register(company)
admin.site.register(category)
