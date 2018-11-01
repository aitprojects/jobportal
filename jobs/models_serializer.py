from rest_framework import serializers
from django.contrib.auth.models import Group , User

from jobs.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username' , 'first_name' , 'last_name')

class SpiderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpiderData
        fields ='__all__'


class UserShortlistedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserShortlisted
        fields ='__all__'


class UserOrBrowserSeenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserOrBrowserSeen
        fields ='__all__'
        
        

class JobsRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobsRelated
        fields ='__all__'



class JobsSerializer(serializers.ModelSerializer):
    jobs_related_to = JobsRelatedSerializer(many = True)
    user_browser_seen = UserOrBrowserSeenSerializer(many = True)
    user_shortlisted = UserShortlistedSerializer(many = True)
    top_condidates = UserSerializer(many = True)

    class Meta:
        model = Jobs
        #fields ='__all__'
        fields = ['id' ,'title',  'user_browser_seen' , 'user_shortlisted' ,'top_condidates','jobs_related_to']
        #depth = 1

class JobsSerializerResume(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        #fields ='__all__'
        fields = ['id' , 'title']
        #depth = 1
        
class JobsSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        #fields ='__all__'
        fields = ['id' , 'title' , 'website']
        #depth = 1

class JobsRelatedSerializer_(serializers.ModelSerializer):
    job = JobsSerializerResume()
    class Meta:
        model = JobsRelated
        fields ='__all__'
        
        


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields ='__all__'
        
        
        
        
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields ='__all__'
        
   
class ExperianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiance
        fields ='__all__'
        
        
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields ='__all__'
        
        
        
        
class UserResumeRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResumeRelated
        fields ='__all__'
        
        
        
        
class UserResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    educations = EducationSerializer(many = True)
    experiances = ExperianceSerializer(many = True)
    languages = LanguageSerializer(many = True)
    skills = SkillsSerializer(many = True)
    top_jobs = JobsSerializer(many = True)
    #resume_related_to = UserResumeRelatedSerializer(many = True)
    
    class Meta:
        model = UserResume
        fields ='__all__'
        
        
        
  
class UserResumeRelatedSerializer_(serializers.ModelSerializer):
   #resumes = UserResumeSerializer()
   class Meta:
       model = UserResumeRelated
       fields ='__all__'
       
       
        
    
