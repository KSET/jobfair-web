import hashlib
import random

from django.db import models, transaction
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail

import base62

YEARS = map(lambda x: (x,x), reversed(range(1930, timezone.now().year)))
YEARS.insert(0, (-1, 'U TIJEKU'))
SKILL_LEVEL = map(lambda x: (x,x), range(1,11))

class UserManager(models.Manager):
    
    def create_user(self, first_name, last_name, email):
        salt = hashlib.sha1(str(random.random())).hexdigest()[:10]
        access_code = base62.encode(
                int(hashlib.md5(first_name_last_name_email+salt), 16)
                )
        new_user = self.create(
                first_name=first_name, 
                last_name=last_name,
                email=email, 
                access_code=access_code
                )
        new_user.send_email()
        return new_user
    
    create_user = transaction.commit_on_success(create_user)


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    access_code = models.CharField(max_length=40)

    def send_email(self):
        subject = render_to_string('cv/email_subject.txt')
        subject = ''.join(subject.splitlines())
        body = render_to_string('cv/email_body.txt', {'access_code': self.access_code})
        send_mail(subject, body, 'jobfair-zivotopisi@kset.org', 
                self.email, fail_silently=False)


class UserDetail(models.Model):
    user = models.ForeignKey(User)
    phone_number = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    web_page = models.CharField(max_length=256)
    date_of_birth = models.DateField()


class Education(models.Model):
    user = models.ForeignKey(User)
    # maybe change this to include choice option
    faculty = models.CharField(max_length=128)
    start_date = models.CharField(max_length=4, choices=YEARS)
    end_date = models.CharField(max_length=4, choices=YEARS)
    program = models.CharField(max_length=64)
    # add possible titles, more research needed
    title = models.CharField(max_length=64)


class EducationActivities(models.Model):
    user = models.ForeignKey(User)
    activity = models.TextField()


class ForeignLanguage(models.Model):
    user = models.ForeignKey(User)
    language = models.CharField(max_length=32)
    reading = models.IntegerField(choices=SKILL_LEVEL)
    speaking = models.IntegerField(choices=SKILL_LEVEL)
    extra_notes = models.TextField()

    
class Experience(models.Model):
    user = models.ForeignKey(User)
    job = models.TextField()


class Skills(models.Model):
    user = models.ForeignKey(User)
    skill = models.CharField(max_length=256)
    description = models.TextField()


class Other(models.Model):
    user = models.ForeignKey(User)
    about_yourself = models.TextField()
    expectations = models.TextField()
    prefered_job = models.TextField()
