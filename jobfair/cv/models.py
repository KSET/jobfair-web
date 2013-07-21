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

class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    access_code = models.CharField(max_length=40, editable=False)

    def save(self, *args, **kwargs):
        salt = hashlib.sha1(str(random.random())).hexdigest()[:10]
        self.access_code = base62.encode(
                int(hashlib.sha1(self.first_name+self.last_name+self.email+salt).hexdigest(), 16)
                )
        super(Person, self).save(*args, **kwargs)

    def send_email(self):
        subject = render_to_string('cv/email_subject.txt')
        subject = ''.join(subject.splitlines())
        body = render_to_string('cv/email_body.txt', {'access_code': self.access_code})
        send_mail(subject, body, 'jobfair-zivotopisi@kset.org', 
                (self.email,), fail_silently=False)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + ", " + self.email

    class Meta():
        ordering = ['last_name', 'first_name', 'email']
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'




class PersonDetail(models.Model):
    person = models.OneToOneField(Person)
    phone_number = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=256, blank=True)
    web_page = models.CharField(max_length=256, blank=True)
    date_of_birth = models.DateField(blank=True)

    def __unicode__(self):
        return self.person.__unicode__() + ": detail"


    class Meta():
        verbose_name = 'Person detail'
        verbose_name_plural = 'Person details'




class Education(models.Model):
    person = models.ForeignKey(Person)
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
    person = models.ForeignKey(Person)
    activity = models.TextField()

    def __unicode__(self):
        return self.person.__unicode__() + " activity"

    class Meta():
        verbose_name = 'Education activity'
        verbose_name_plural = 'Education activities'




class ForeignLanguage(models.Model):
    person = models.ForeignKey(Person)
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
    person = models.ForeignKey(Person)
    job = models.TextField()

    def __unicode__(self):
        return self.person.__unicode__() + ": job"

    class Meta():
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'




class Skills(models.Model):
    person = models.ForeignKey(Person)
    skill = models.CharField(max_length=256)
    description = models.TextField()

    def __unicode__(self):
        return self.person.__unicode__() + ": " + self.skill

    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'




class Other(models.Model):
    person = models.OneToOneField(Person)
    about_yourself = models.TextField(blank=True)
    expectations = models.TextField(blank=True)
    prefered_job = models.TextField(blank=True)

    def __unicode__(self):
        return self.person.__unicode__() + ": other"

    class Meta():
        verbose_name = 'Other'
        verbose_name_plural = 'Others'


