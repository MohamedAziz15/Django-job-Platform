from django.contrib import admin
from .models import category, company, job


class jobadmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'Location',
                    'vacancy', 'job_type', 'category']
    search_fields = ('title', 'category', 'description')
    list_filter = ('vacancy', 'job_type', 'category', 'experience')


admin.site.register(job, jobadmin)
admin.site.register(company)
admin.site.register(category)
