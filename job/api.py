from .serializer import jobSerializer
from .models import job

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
 
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


@api_view(['GET'])
def job_list_api(request):

    jobs = job.objects.all()
    data = jobSerializer(jobs, many=True).data
    return Response({'jobs': data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_ = job.objects.get(id=id)
    data = jobSerializer(job_,many=False).data
    return Response({'job': data})

#Class based view
class JobListAPI(generics.ListAPIView):
    queryset = job.objects.all()
    serializer_class = jobSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields  = ['title','vacancy','job_type']
    search_fields = ['title', 'description']
    ordering_fields = ['salary_start', 'salary_end','experience']





class JobDetailAPI(generics.RetrieveAPIView,RetrieveUpdateDstroyAPIView):
    queryset = job.objects.all()
    serializer_class = jobSerializer