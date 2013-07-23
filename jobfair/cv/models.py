import hashlib
import random
import string

from django.db import models, transaction
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.models import User as AuthUser 

YEARS = map(lambda x: (x,x), reversed(range(1930, timezone.now().year)))
YEARS.insert(0, (-1, 'U TIJEKU'))
SKILL_LEVEL = map(lambda x: (x,x), range(1,11))

class User(AuthUser):

    def save(self, *args, **kwargs):
        self.password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        self.username = kwargs['email']
        super(ProxyUser, self).save(*args, **kwargs)

    def send_email(self):
        subject = render_to_string('cv/email_subject.txt')
        subject = ''.join(subject.splitlines())
        body = render_to_string('cv/email_body.txt', {'access_code': self.access_code})
        send_mail(subject, body, 'jobfair-zivotopisi@kset.org', 
                (self.email,), fail_silently=False)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + ", " + self.email

    class Meta():
        proxy = 'True'




class UserDetail(models.Model):
    person = models.OneToOneField(User)
    phone_number = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=256, blank=True)
    web_page = models.CharField(max_length=256, blank=True)
    date_of_birth = models.DateField(blank=True)

    def __unicode__(self):
        return self.person.__unicode__() + ": detail"


    class Meta():
        verbose_name = 'User detail'
        verbose_name_plural = 'User details'




class Education(models.Model):
    person = models.ForeignKey(User)
    # maybe change this to include choice option
    faculty = models.CharField(max_length=128)
    start_date = models.CharField(max_length=4, choices=YEARS)
    end_date = models.CharField(max_length=4, choices=YEARS)
    program = models.CharField(max_length=64)
    # add possible titles, more research needed
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return self.person.__unicode__() + ": " + self.faculty

    class Meta():
        verbose_name = 'Education'
        verbose_name_plural = 'Education'



class EducationActivities(models.Model):
    person = models.ForeignKey(User)
    activity = models.TextField()

    def __unicode__(self):
        return self.person.__unicode__() + " activity"

    class Meta():
        verbose_name = 'Education activity'
        verbose_name_plural = 'Education activities'




class ForeignLanguage(models.Model):
    person = models.ForeignKey(User)
    language = models.CharField(max_length=32)
    reading = models.IntegerField(choices=SKILL_LEVEL)
    speaking = models.IntegerField(choices=SKILL_LEVEL)
    extra_notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.person.__unicode__() + ": " + self.language

    class Meta():
        verbose_name = 'Foreign language'
        verbose_name_plural = 'Foreign languages'



    
class Experience(models.Model):
    person = models.ForeignKey(User)
    job = models.TextField()

    def __unicode__(self):
        return self.person.__unicode__() + ": job"

    class Meta():
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'




class Skills(models.Model):
    person = models.ForeignKey(User)
    skill = models.CharField(max_length=256)
    description = models.TextField()

    def __unicode__(self):
        return self.person.__unicode__() + ": " + self.skill

    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'




class Other(models.Model):
    person = models.OneToOneField(User)
    about_yourself = models.TextField(blank=True)
    expectations = models.TextField(blank=True)
    prefered_job = models.TextField(blank=True)

    def __unicode__(self):
        return self.person.__unicode__() + ": other"

    class Meta():
        verbose_name = 'Other'
        verbose_name_plural = 'Others'


