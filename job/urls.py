from django.urls import path
from .views import job_list, job_detail, jobApply , addJob
from .api import job_list_api , job_detail_api, JobListAPI , JobDetailAPI


urlpatterns = [
    path('', job_list),
    path('Add/', addJob.as_view()),
    path('<slug:slug>',job_detail),
    path('<slug:slug>/apply',jobApply.as_view()),

    
#API as functions
    #path('api/list',job_list_api),
    #path('api/list/<int:id>/',job_detail_api),

#API as class based view
    path('api/list',JobListAPI.as_view()),
    path('api/list/<int:id>/',JobDetailAPI.as_view()),

]


