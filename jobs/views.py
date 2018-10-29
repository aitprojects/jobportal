from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response



from jobs.models_serializer import *
from jobs.decorators import *


@api_view(['GET' , 'POST'])
@unique_user_decorator
def job(request , id):
    job = get_object_or_404(Jobs , id = id)
    job_ser = JobsSerializer(job).data
    job_ser['jobs_related_to'] = JobsRelatedSerializer_(job.jobs_related_to.all().order_by('weight') , many=True).data
    return Response(job_ser)


@api_view(['GET' , 'POST'])
def job_list(request):
    job = Jobs.objects.all().order_by('-open_date')
    job_ser = JobsSerializer(job , many=True).data
    return Response(job_ser)








@api_view(['GET' , 'POST'])
@unique_user_decorator
def userresume(request , id):
    resume = get_object_or_404(UserResume , id = id)
    resume_ser = UserResumeSerializer(resume).data
    resume_ser['resume_related_to'] = UserResumeRelatedSerializer_(resume.resume_related_to.all().order_by('weight')[:10] , many=True).data
    resume_ser['top_jobs'] = JobsSerializerResume(resume.user.jobs_set.all()[:10] , many=True).data
    return Response(resume_ser)