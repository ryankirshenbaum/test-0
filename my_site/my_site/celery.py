import os

from celery import Celery
from .settings import CELERY_BROKER_URL
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_site.settings'

django_url = CELERY_BROKER_URL
app = Celery('test_app', broker=django_url, result_backend=django_url)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def create(self):
    print(f'Request: {self.request!r}')