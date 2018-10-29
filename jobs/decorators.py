import functools
from jobs.models import *


def eval_token():
    return 'KJSHDKSJDKWLDKDHW'



def unique_user_decorator(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        print(kwargs)
        request = args[0]
        job_id = kwargs['id']
        job = Jobs.objects.get(id=job_id)
        seen = job.user_browser_seen.filter(token=request.COOKIES.get('user_token')).exists()

        response = func(*args , **kwargs)
        try:
            if seen is False:
                obj = UserOrBrowserSeen(token=request.COOKIES.get('user_token'))
                obj.save()
                job.user_browser_seen.add(obj)
                job.save()

        except:
            new_token = eval_token()
            response.set_cookie('user_token', new_token)
            obj = UserOrBrowserSeen(token=new_token)
            obj.save()
            job.user_browser_seen.add(obj)
            job.save()
        return response

    return wrapper