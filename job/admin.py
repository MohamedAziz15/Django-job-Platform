from django.contrib import admin
from .models import category, company, job


admin.site.register(job)
admin.site.register(company)
admin.site.register(category)
