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

    class Meta():
        ordering = ['last_name', 'first_name', 'email']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserDetail(models.Model):
    user = models.OneToOne(User)
    phone_number = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=256, blank=True)
    web_page = models.CharField(max_length=256, blank=True)
    date_of_birth = models.DateField(blank=True)

    class Meta():
        verbose_name = 'User detail'
        verbose_name_plural = 'Users details'


class Education(models.Model):
    user = models.ForeignKey(User)
    # maybe change this to include choice option
    faculty = models.CharField(max_length=128)
    start_date = models.CharField(max_length=4, choices=YEARS)
    end_date = models.CharField(max_length=4, choices=YEARS)
    program = models.CharField(max_length=64)
    # add possible titles, more research needed
    title = models.CharField(max_length=64)

    class Meta():
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class EducationActivities(models.Model):
    user = models.ForeignKey(User)
    activity = models.TextField()

    class Meta():
        verbose_name = 'Education activity'
        verbose_name_plural = 'Education activities'


class ForeignLanguage(models.Model):
    user = models.ForeignKey(User)
    language = models.CharField(max_length=32)
    reading = models.IntegerField(choices=SKILL_LEVEL)
    speaking = models.IntegerField(choices=SKILL_LEVEL)
    extra_notes = models.TextField(blank=True)

    class Meta():
        verbose_name = 'Foreign language'
        verbose_name_plural = 'Foreign languages'

    
class Experience(models.Model):
    user = models.ForeignKey(User)
    job = models.TextField()

    class Meta():
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class Skills(models.Model):
    user = models.ForeignKey(User)
    skill = models.CharField(max_length=256)
    description = models.TextField()

    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Other(models.Model):
    user = models.OneToOne(User)
    about_yourself = models.TextField(blank=True)
    expectations = models.TextField(blank=True)
    prefered_job = models.TextField(blank=True)

    class Meta():
        verbose_name = 'Other'
        verbose_name_plural = 'Others'
