from celery import shared_task
import logging
import os
from .models import Member
from django.contrib.auth.models import User
from my_site.celery import app
from celery.utils.log import get_task_logger
from django.conf import settings



logger = get_task_logger(__name__)

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_site.settings'

@app.task
def create_member(username, password, gender, country):
    logger.info('Creating member {}.'.format(username))
    member = Member()
    user = User.objects.create_user(username, password)
    member.user = user
    member.gender = gender
    member.country = country
    member.save()
    return 'hello world'