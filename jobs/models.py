from django.db import models
from django.utils import six, timezone
from django.http import  HttpRequest
from django.contrib.auth.models import User
from django.utils.text import Truncator




class Education(models.Model):
    id = models.AutoField( primary_key=True)  # Field name made lowercase.
    univercity = models.CharField(  max_length=45, blank=True, null=True ,default="Where Did You Learn ?")  # Field name made lowercase.
    start_date = models.DateField(  blank=True, null=True , default=timezone.now)  # Field name made lowercase.
    end_date = models.DateField(  blank=True, null=True, default=timezone.now)  # Field name made lowercase.
    degree = models.CharField(  max_length=45, blank=True, null=True ,default="Which Degree Did You Earn ?")  # Field name made lowercase.
    descriptions = models.CharField(  max_length=250, blank=True, null=True ,default="Description about education")  # Field name made lowercase.
    
    def __str__(self):
        trancate = Truncator(self.descriptions)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.descriptions)
        return trancate.words(5)
    

class Experiance(models.Model):
    company = models.CharField(  max_length=45, blank=True, null=True ,default='Where Did You Work')  # Field name made lowercase.
    start_date = models.DateTimeField(  blank=True, null=True,default=timezone.now)  # Field name made lowercase.
    end_date = models.DateTimeField(  blank=True, null=True,default=timezone.now)  # Field name made lowercase.
    description = models.CharField(  max_length=250, blank=True, null=True,default='Say Something About Your Job')  # Field name made lowercase.
    
    def __str__(self):
        trancate = Truncator(self.description)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.description)
        return trancate.words(5)

class Language(models.Model):
    language = models.CharField(  max_length=45, blank=True, null=True)  # Field name made lowercase.
    percent = models.IntegerField(  blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        trancate = Truncator(self.language)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.language)
        return trancate.words(5)

class Skills(models.Model):
    skill = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    percent = models.IntegerField(  blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        trancate = Truncator(self.skill)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.skill)
        return trancate.words(5)


class UserResumeRelated(models.Model):
    id = models.AutoField(primary_key=True)
    resumes = models.ForeignKey('UserResume', models.DO_NOTHING,   blank=True, null=True , related_name="userresume_related")
    weight_des = models.FloatField(blank=True, null=True ,default = 0)
    weight_req = models.FloatField(blank=True, null=True ,default = 0)
    weight = models.FloatField(blank=True, null=True ,default = 0)
    
    def __str__(self):
        trancate = Truncator(self.resume.user.username)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.resume.user.username)
        return trancate.words(5)


    def save(self, *args, **kwargs):
        self.weight = self.weight_des + self.weight_req
        return super(UserResumeRelated, self).save(*args, **kwargs)

    class Meta:
        ordering = ['weight']
        
        
class UserResume(models.Model):
    id = models.AutoField( primary_key=True)  # Field name made lowercase.
    user = models.OneToOneField(User, models.DO_NOTHING,   blank=True, null=True , related_name="resume")  # Field name made lowercase.
    interst_and_activites = models.CharField( max_length=500, blank=True, null=True, default="say something about yourself ")  # Field name made lowercase.
    profession = models.CharField(  max_length=300, blank=True, null=True , default="Proffession ?")  # Field name made lowercase.
    email = models.CharField(  max_length=45, blank=True, null=True,default='YourEmail@example.com')  # Field name made lowercase.
    phone = models.CharField(  max_length=45, blank=True, null=True, default='9300')  # Field name made lowercase.
    tags = models.CharField(  max_length=250, blank=True, null=True, default="no tags")  # Field name made lowercase.
    address = models.CharField(  max_length=250, blank=True, null=True , default="no address")  # Field name made lowercase.
    direction = models.CharField(  max_length=45, blank=True, null=True , default="nod")
    resume = models.FileField('resume', max_length=128  ,upload_to = 'resume/uploaded/', default = 'defaults.doc')
    resume_related_to = models.ManyToManyField(UserResumeRelated)
    educations = models.ManyToManyField(Education)
    experiances = models.ManyToManyField(Experiance)
    languages = models.ManyToManyField(Language)
    skills = models.ManyToManyField(Skills)
    
    
    
    
    top_jobs = models.ManyToManyField('Jobs')
    
    def __str__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)






class SpiderData(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.CharField(max_length=50, default='0')
    title = models.CharField(max_length=50, default='0')
    organization = models.CharField(max_length=50, default='0')
    about_company = models.CharField(max_length=8000, default='0')
    job_description = models.CharField(max_length=8000, default='0')
    open_date = models.CharField(max_length=50, default='0')
    closing_date = models.CharField(max_length=50, default='0')
    number_vacancies = models.CharField(max_length=50, default='0')
    functional_area = models.CharField(max_length=50, default='0')
    nationality = models.CharField(max_length=50, default='0')
    contract_type = models.CharField(max_length=50, default='0')
    contract_duration = models.CharField(max_length=50, default='0')
    probation_period = models.CharField(max_length=50, default='0')
    reference = models.CharField(max_length=50, default='0')
    work_type = models.CharField(max_length=50, default='0')
    gender = models.CharField(max_length=20, default='0')
    open_ended = models.CharField(max_length=50, default='0')
    salary_range = models.CharField(max_length=50, default='0')
    year_of_expirence = models.CharField(max_length=50, default='0')
    extension_passibility = models.CharField(max_length=50, default='0')
    duties_responsibilities = models.CharField(max_length=8000, default='0')
    skills = models.CharField(max_length=8000, default='0')
    qualification = models.CharField(max_length=8000, default='0')
    jobs_location = models.CharField(max_length=8000, default='0')
    education = models.CharField(max_length=100, default='0')
    submission_guideline = models.CharField(max_length=8000, default='0')
    submission_email = models.CharField(max_length=50, default='0')
    website = models.CharField(max_length=50, default='0')
    deleted = models.BooleanField(default = False)
    active = models.BooleanField(default = True)
    def __str__(self):
        trancate = Truncator(self.title)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.title)
        return trancate.words(5)



class UserShortlisted(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    token = models.CharField(max_length=512, default='0')
    user =models.ForeignKey(User, models.DO_NOTHING,   blank=True, null=True)
    
    def __str__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    
    class Meta:
        index_together = ['token']


class UserApplaid(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    token = models.CharField(max_length=512, default='0')
    user =models.ForeignKey(User, models.DO_NOTHING,   blank=True, null=True)
    
    def __str__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    
    class Meta:
        index_together = ['token']
        
        
        
class UserAbuse(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    token = models.CharField(max_length=512, default='0')
    user =models.ForeignKey(User, models.DO_NOTHING,   blank=True, null=True)
    
    def __str__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    
    class Meta:
        index_together = ['token']
        
        
        
class UserOrBrowserSeen(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    token = models.CharField(max_length=512, default='0')
    user =models.ForeignKey(User, models.DO_NOTHING,   blank=True, null=True)
    
    def __str__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.user.username)
        return trancate.words(5)
    
    
    class Meta:
        index_together = ['token']

class JobsRelated(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey('Jobs', models.DO_NOTHING,   blank=True, null=True , related_name="jobs_related")
    weight_des = models.FloatField(blank=True, null=True ,default = 0)
    weight_req = models.FloatField(blank=True, null=True ,default = 0)
    weight = models.FloatField(blank=True, null=True ,default = 0)
    
    
    def __str__(self):
        trancate = Truncator(self.job.title)
        return trancate.words(5)
    
    def __repr__(self):
        trancate = Truncator(self.job.title)
        return trancate.words(5)

    def save(self, *args, **kwargs):
        self.weight = self.weight_des + self.weight_req
        return super(JobsRelated, self).save(*args, **kwargs)

    class Meta:
        ordering = ['weight']




class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.CharField(max_length=50, default='0')
    title = models.CharField(max_length=50, default='0')
    organization = models.CharField(max_length=50, default='0')
    about_company = models.CharField(max_length=8000, default='0')
    job_description = models.CharField(max_length=8000, default='0')
    open_date = models.CharField(max_length=50, default='0')
    closing_date = models.CharField(max_length=50, default='0')
    number_vacancies = models.CharField(max_length=50, default='0')
    functional_area = models.CharField(max_length=50, default='0')
    nationality = models.CharField(max_length=50, default='0')
    contract_type = models.CharField(max_length=50, default='0')
    contract_duration = models.CharField(max_length=50, default='0')
    probation_period = models.CharField(max_length=50, default='0')
    reference = models.CharField(max_length=50, default='0')
    work_type = models.CharField(max_length=50, default='0')
    gender = models.CharField(max_length=20, default='0')
    open_ended = models.CharField(max_length=50, default='0')
    salary_range = models.CharField(max_length=50, default='0')
    year_of_expirence = models.CharField(max_length=50, default='0')
    extension_passibility = models.CharField(max_length=50, default='0')
    duties_responsibilities = models.CharField(max_length=8000, default='0')
    skills = models.CharField(max_length=8000, default='0')
    qualification = models.CharField(max_length=8000, default='0')
    jobs_location = models.CharField(max_length=8000, default='0')
    education = models.CharField(max_length=100, default='0')
    submission_guideline = models.CharField(max_length=8000, default='0')
    submission_email = models.CharField(max_length=50, default='0')
    website = models.CharField(max_length=50, default='0')
    deleted = models.BooleanField(default = False)
    active = models.BooleanField(default = True)
    jobs_related_to = models.ManyToManyField(JobsRelated)
    user_browser_seen = models.ManyToManyField(UserOrBrowserSeen)
    user_applaid = models.ManyToManyField(UserApplaid)
    user_shortlisted = models.ManyToManyField(UserShortlisted)
    user_abuse = models.ManyToManyField(UserAbuse)
    top_condidates = models.ManyToManyField(User)
    
    
    def __str__(self):
        trancate = Truncator(self.title)
        return trancate.words(5)
    def __repr__(self):
        trancate = Truncator(self.title)
        return trancate.words(5)



    @property
    def is_shortlisted(self , request = HttpRequest()):
        if request.user.is_anonymous:
            return self.user_browser_seen.filter(token = request.COOKIES.get('user_token')).exists()
        else:
            return self.user_browser_seen.filter(user = request.user).exists()
        
    @property
    def is_applaid(self , request = HttpRequest()):
        if request.user.is_anonymous:
            return self.user_abuse.filter(token = request.COOKIES.get('user_token')).exists()
        else:
            return self.user_abuse.filter(user=request.user).exists()
        
        
    @property
    def is_abuse(self , request = HttpRequest()):
        if request.user.is_anonymous:
            return self.user_applaid.filter(token = request.COOKIES.get('user_token')).exists()
        else:
            return self.user_applaid.filter(user=request.user).exists()
        
        
        
    @property
    def is_expired(self):
        return self.closing_date < timezone.now()
    
    @property
    def is_active(self):
        return not self.active


    @property
    def get_number_of_unique_seen(self):
        return self.user_browser_seen.count()
    
    @property
    def get_number_of_unique_seen(self):
        return self.user_browser_seen.count()


    @property
    def get_number_of_shortlisted(self):
        return self.user_browser_seen.count()


    class Meta:
        index_together = ["job_description", "duties_responsibilities"]




