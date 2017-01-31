# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Other.person'
        db.alter_column(u'cv_other', 'person_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cv.Person'], unique=True))
        # Adding unique constraint on 'Other', fields ['person']
        db.create_unique(u'cv_other', ['person_id'])


        # Changing field 'PersonDetail.person'
        db.alter_column(u'cv_persondetail', 'person_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cv.Person'], unique=True))
        # Adding unique constraint on 'PersonDetail', fields ['person']
        db.create_unique(u'cv_persondetail', ['person_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PersonDetail', fields ['person']
        db.delete_unique(u'cv_persondetail', ['person_id'])

        # Removing unique constraint on 'Other', fields ['person']
        db.delete_unique(u'cv_other', ['person_id'])


        # Changing field 'Other.person'
        db.alter_column(u'cv_other', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

        # Changing field 'PersonDetail.person'
        db.alter_column(u'cv_persondetail', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

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
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cv.Person']", 'unique': 'True'}),
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
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cv.Person']", 'unique': 'True'}),
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