from jobs.models import *
from django.contrib import admin


class AdminJobs(admin.ModelAdmin):
    list_display = ('id','title' ,'organization')
    fields = ('title','organization' , 'job_description' ,'voccancy_number', 'submission_email')
    
    
class AdminUserResume(admin.ModelAdmin):
    list_display = ('id','user' ,'profession')
    fields = ('user','interst_and_activites' , 'profession' ,'email', 'phone'
              , 'tags' , 'address' , 'educations','experiances','languages','skills'
              )
    

admin.site.register(Jobs,AdminJobs)
admin.site.register(Education)
admin.site.register(Experiance)
admin.site.register(Language)
admin.site.register(Skills)
admin.site.register(UserResume , AdminUserResume)