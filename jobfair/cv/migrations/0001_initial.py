# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'cv_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('access_code', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'cv', ['Person'])

        # Adding model 'PersonDetail'
        db.create_table(u'cv_persondetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('web_page', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'cv', ['PersonDetail'])

        # Adding model 'Education'
        db.create_table(u'cv_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('faculty', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('start_date', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('end_date', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'cv', ['Education'])

        # Adding model 'EducationActivities'
        db.create_table(u'cv_educationactivities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('activity', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cv', ['EducationActivities'])

        # Adding model 'ForeignLanguage'
        db.create_table(u'cv_foreignlanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('reading', self.gf('django.db.models.fields.IntegerField')()),
            ('speaking', self.gf('django.db.models.fields.IntegerField')()),
            ('extra_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'cv', ['ForeignLanguage'])

        # Adding model 'Experience'
        db.create_table(u'cv_experience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('job', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cv', ['Experience'])

        # Adding model 'Skills'
        db.create_table(u'cv_skills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cv', ['Skills'])

        # Adding model 'Other'
        db.create_table(u'cv_other', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person'])),
            ('about_yourself', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('expectations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('prefered_job', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'cv', ['Other'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'cv_person')

        # Deleting model 'PersonDetail'
        db.delete_table(u'cv_persondetail')

        # Deleting model 'Education'
        db.delete_table(u'cv_education')

        # Deleting model 'EducationActivities'
        db.delete_table(u'cv_educationactivities')

        # Deleting model 'ForeignLanguage'
        db.delete_table(u'cv_foreignlanguage')

        # Deleting model 'Experience'
        db.delete_table(u'cv_experience')

        # Deleting model 'Skills'
        db.delete_table(u'cv_skills')

        # Deleting model 'Other'
        db.delete_table(u'cv_other')


    models = {
        u'cv.education': {
            'Meta': {'object_name': 'Education'},
            'end_date': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'start_date': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cv.educationactivities': {
            'Meta': {'object_name': 'EducationActivities'},
            'activity': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"})
        },
        u'cv.experience': {
            'Meta': {'object_name': 'Experience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.TextField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"})
        },
        u'cv.foreignlanguage': {
            'Meta': {'object_name': 'ForeignLanguage'},
            'extra_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"}),
            'reading': ('django.db.models.fields.IntegerField', [], {}),
            'speaking': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cv.other': {
            'Meta': {'object_name': 'Other'},
            'about_yourself': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expectations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"}),
            'prefered_job': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'cv.person': {
            'Meta': {'ordering': "['last_name', 'first_name', 'email']", 'object_name': 'Person'},
            'access_code': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cv.persondetail': {
            'Meta': {'object_name': 'PersonDetail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'web_page': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'cv.skills': {
            'Meta': {'object_name': 'Skills'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cv.Person']"}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['cv']