import os
from celery import Celery
from celery.schedules import timedelta as celery_timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'process-cbr-every-hour': {
        'task': 'currency.tasks.process_cbr_request',
        'schedule': celery_timedelta(seconds=10),
    },
}
