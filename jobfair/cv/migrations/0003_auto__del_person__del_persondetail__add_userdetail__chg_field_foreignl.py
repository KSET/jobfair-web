# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'cv_person')

        # Deleting model 'PersonDetail'
        db.delete_table(u'cv_persondetail')

        # Adding model 'UserDetail'
        db.create_table(u'cv_userdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('web_page', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'cv', ['UserDetail'])


        # Changing field 'ForeignLanguage.person'
        db.alter_column(u'cv_foreignlanguage', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Skills.person'
        db.alter_column(u'cv_skills', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'EducationActivities.person'
        db.alter_column(u'cv_educationactivities', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Other.person'
        db.alter_column(u'cv_other', 'person_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # Changing field 'Education.person'
        db.alter_column(u'cv_education', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Experience.person'
        db.alter_column(u'cv_experience', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'cv_person', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_code', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, unique=True)),
        ))
        db.send_create_signal(u'cv', ['Person'])

        # Adding model 'PersonDetail'
        db.create_table(u'cv_persondetail', (
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('web_page', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('person', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cv.Person'], unique=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cv', ['PersonDetail'])

        # Deleting model 'UserDetail'
        db.delete_table(u'cv_userdetail')


        # Changing field 'ForeignLanguage.person'
        db.alter_column(u'cv_foreignlanguage', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

        # Changing field 'Skills.person'
        db.alter_column(u'cv_skills', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

        # Changing field 'EducationActivities.person'
        db.alter_column(u'cv_educationactivities', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

        # Changing field 'Other.person'
        db.alter_column(u'cv_other', 'person_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cv.Person'], unique=True))

        # Changing field 'Education.person'
        db.alter_column(u'cv_education', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

        # Changing field 'Experience.person'
        db.alter_column(u'cv_experience', 'person_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cv.Person']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cv.education': {
            'Meta': {'object_name': 'Education'},
            'end_date': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'start_date': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'cv.educationactivities': {
            'Meta': {'object_name': 'EducationActivities'},
            'activity': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cv.experience': {
            'Meta': {'object_name': 'Experience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.TextField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cv.foreignlanguage': {
            'Meta': {'object_name': 'ForeignLanguage'},
            'extra_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'reading': ('django.db.models.fields.IntegerField', [], {}),
            'speaking': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cv.other': {
            'Meta': {'object_name': 'Other'},
            'about_yourself': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expectations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'prefered_job': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'cv.skills': {
            'Meta': {'object_name': 'Skills'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'cv.userdetail': {
            'Meta': {'object_name': 'UserDetail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'web_page': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['cv']