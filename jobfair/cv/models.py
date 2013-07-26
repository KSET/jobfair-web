import hashlib
import random
import string

from django.db import models, transaction
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.models import User as AuthUser 

YEARS_BEGIN = map(lambda x: (x,x), reversed(range(1930, timezone.now().year+1)))
YEARS_END = map(lambda x: (x,x), reversed(range(1930, timezone.now().year+30)))
YEARS_END.insert(0, (-1, 'U TIJEKU'))
SKILL_LEVEL = map(lambda x: (x,x), range(1,11))

class User(AuthUser):

    def save(self, *args, **kwargs):
        password = User.objects.make_random_password()
        self.set_password(password)
        self.username = self.email
        super(User, self).save(*args, **kwargs)
        # not yet implemented
#        self.send_email(password)

    def send_email(self, password):
        subject = render_to_string('cv/email_subject.txt')
        subject = ''.join(subject.splitlines())
        body = render_to_string('cv/email_body.txt', {'password': password})
        send_mail(subject, body, 'jobfair-zivotopisi@kset.org', 
                (self.email,), fail_silently=False)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + ", " + self.email

    class Meta():
        proxy = 'True'


class UserDetail(models.Model):
    user = models.OneToOneField(User, editable=False)
    phone_number = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=256, blank=True)
    web_page = models.CharField(max_length=256, blank=True)
    date_of_birth = models.DateField(blank=True)

    def __unicode__(self):
        return str(self.user) + ': detail'


    class Meta():
        verbose_name = 'User detail'
        verbose_name_plural = 'User details'


class Education(models.Model):
    user = models.ForeignKey(User)
    # maybe change this to include choice option
    faculty = models.CharField(max_length=128)
    start = models.IntegerField(choices=YEARS_BEGIN)
    end = models.IntegerField(choices=YEARS_END)
    program = models.CharField(max_length=64)
    # add possible titles, more research needed
    title = models.CharField(max_length=64)
    extra_activities = models.TextField()

    def __unicode__(self):
        return str(self.user) + self.faculty

    class Meta():
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class ForeignLanguage(models.Model):
    user = models.ForeignKey(User)
    language = models.CharField(max_length=32)
    reading = models.IntegerField(choices=SKILL_LEVEL)
    speaking = models.IntegerField(choices=SKILL_LEVEL)
    extra_notes = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.user) + self.language

    class Meta():
        verbose_name = 'Foreign language'
        verbose_name_plural = 'Foreign languages'



    
class Experience(models.Model):
    user = models.ForeignKey(User)
    job = models.TextField()

    def __unicode__(self):
        return str(self.user) + ": job"

    class Meta():
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'




class Skills(models.Model):
    user = models.ForeignKey(User)
    skill = models.CharField(max_length=256)
    description = models.TextField()

    def __unicode__(self):
        return str(self.user) + ": " + self.skill

    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'




class Other(models.Model):
    user = models.OneToOneField(User)
    about_yourself = models.TextField(blank=True)
    expectations = models.TextField(blank=True)
    prefered_job = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.user) + ": other"

    class Meta():
        verbose_name = 'Other'
        verbose_name_plural = 'Others'


