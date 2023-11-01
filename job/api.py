from .serializer import jobSerializer
from .models import job

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def job_list_api(request):

    jobs = job.objects.all()
    data = jobSerializer(jobs, many=True).data
    return Response({'jobs': data})
