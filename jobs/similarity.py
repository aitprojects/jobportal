import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
from jobs.models import *
from django.contrib.auth.models import User
import csv
from django.core import serializers
from django.forms.models import model_to_dict


from sklearn.neighbors import NearestNeighbors
import pandas as pd
import sys
#import wikipedia
import csv

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


def transfer_data():
    data = SpiderData.objects.all()
    print('Please wait we are transfering data for jobs' , end='\n')
    printProgressBar(0, len(data), prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    for index , job in enumerate(data):
        printProgressBar(index+1, len(data), prefix = 'Progress:', suffix = 'Complete', length = 50)
        j = Jobs(**model_to_dict(job))
        j.save()
        
    

def prepare_job_csv_file():
    csvfile = open('similar_jobs.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['source', 'target'])
    jobs = Jobs.objects.all()
    
    print('Please wait we are preparing csv file for jobs' , end='\n')
    printProgressBar(0, len(jobs), prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    for index , job in enumerate(jobs):
        printProgressBar(index+1, len(jobs), prefix = 'Progress:', suffix = 'Complete', length = 50)
        
        job_id = job.id
        #result = model_to_dict(job)
        
        job_des = job.title
        job_des +=' '+ job.job_description
        job_des +=' '+job.duties_responsibilities
        job_des +=' '+job.functional_area
        job_des +=' '+ job.qualification
        writer.writerow([job_id, str(job_des.encode('utf-8'))])
    csvfile.close()
    
    
    
def prepare_user_csv_file():
    
    csvfile = open('similar_users.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['source', 'target'])
    users = User.objects.all()
    
    print('please wait we are preparing csv file for users.', end='\n')
    printProgressBar(0, len(users), prefix = 'Progress:', suffix = 'Complete', length = 50)
    for index , user in enumerate(users):
        printProgressBar(index+1, len(users), prefix = 'Progress:', suffix = 'Complete', length = 50)
        
        id = user.id + 10000001
        educations = user.resume.educations.values_list('degree', flat=True)
        experiances = user.resume.experiances.values_list('description', flat=True)
        languages = user.resume.languages.values_list('language', flat=True)
        skills = user.resume.skills.values_list('skill', flat=True)
        result = ' '+' '.join(list(educations))
        result +=' '+' '.join(list(experiances))
        result +=' '+' '.join(list(languages))
        result +=' '+' '.join(list(skills))
        writer.writerow([id, result])
    csvfile.close()





def get_tfidf_matrix(dataset):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset)
    return tfidf_matrix

def get_closest_neighs(word, tfidf_matrix , dataset , classes = 10):
    nbrs = NearestNeighbors(n_neighbors=classes).fit(tfidf_matrix)
    row = dataset.index.get_loc(word)
    distances, indices = nbrs.kneighbors(tfidf_matrix.getrow(row))
    names_similar = pd.Series(indices.flatten()).map(dataset.reset_index()['source'])
    #result = pd.DataFrame({'distance':distances.flatten(), 'name':names_similar})
    return zip(distances.flatten() , names_similar)


def calculate_job_similarities():
    
    dataset = pd.read_csv('similar_jobs.csv', index_col='source')['target']
    tfidf_matrix = get_tfidf_matrix(dataset)
    jobs = Jobs.objects.values_list('id', flat=True)
    
    print('please wait we are calculating job similarity it will take few minutes.', end='\n')
    printProgressBar(0, len(jobs), prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    for index , job_id in enumerate(jobs):
        printProgressBar(index+1, len(jobs), prefix = 'Progress:', suffix = 'Complete', length = 50)
        
        similar = get_closest_neighs(job_id, tfidf_matrix , dataset)
        c_job = Jobs.objects.get(id =job_id )
        for v,i in similar:
            p_job = Jobs.objects.get(id =i )
            obj3 = JobsRelated(weight_des = v , job = p_job)
            obj3.save()
            c_job.jobs_related_to.add(obj3)
            c_job.save()
            
            
            
def calculate_user_similarities():
   
    dataset = pd.read_csv('similar_users.csv', index_col='source')['target']
    tfidf_matrix = get_tfidf_matrix(dataset)
    users = User.objects.values_list('id', flat=True)
    
    print('please wait we are calculating user similarity it will take few minutes.', end='\n')
    printProgressBar(0, len(users), prefix = 'Progress:', suffix = 'Complete', length = 50)
    for index , user in enumerate(users):
        printProgressBar(index+1, len(users), prefix = 'Progress:', suffix = 'Complete', length = 50)
        
        similar = get_closest_neighs(user+10000001, tfidf_matrix , dataset , classes = 2)
        c_job = User.objects.get(id =user).resume
        for v,i in similar:
            p_job = User.objects.get(id =i - 10000001 )
            obj3 = UserResumeRelated(weight_des = v , resumes = p_job.resume)
            obj3.save()
            c_job.resume_related_to.add(obj3)
            c_job.save()
        
        
        
def find_job_condidates():
    
    users = pd.read_csv('similar_users.csv', index_col='source')['target']
    jobss = pd.read_csv('similar_jobs.csv', index_col='source')['target']
    
    jobs = Jobs.objects.values_list('id', flat=True)
    
    print('please wait we are finding condidates for jobs it will take few minutes.', end='\n')
    printProgressBar(0, len(jobs), prefix = 'Progress:', suffix = 'Complete', length = 50)
    for index , job_id in enumerate(jobs):
        printProgressBar(index+1, len(jobs), prefix = 'Progress:', suffix = 'Complete', length = 50)
        
        dataset = pd.concat([jobss[jobss.index == job_id] , users])
        tfidf_matrix = get_tfidf_matrix(dataset)
        similar = get_closest_neighs(job_id, tfidf_matrix , dataset , classes = 3)
        c_job = Jobs.objects.get(id =job_id )
        for v,i in similar:
            if v > 0:
                p_job = User.objects.get(id =i - 10000001)
                c_job.top_condidates.add(p_job)
                c_job.save()
                
            


def run_ml_codes():
    transfer_data()
    prepare_job_csv_file()
    prepare_user_csv_file()
    calculate_job_similarities()
    calculate_user_similarities()
    find_job_condidates()
    













