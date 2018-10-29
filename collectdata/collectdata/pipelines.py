import sys
import os
import django

sys.path.extend(['C:\\New_Django_Projects\\jobsportal'])
sys.path.extend(['C:\\New_Django_Projects\\jobsportal\\jobs'])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobsportal.settings")
django.setup()
from jobs.models import SpiderData

class CollectdataPipeline(object):
    def process_item(self, item, spider):
        item_database = SpiderData(**item)
        item_database.save()
        return item
