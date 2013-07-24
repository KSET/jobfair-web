# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EducationActivities'
        db.delete_table(u'cv_educationactivities')

        # Deleting field 'ForeignLanguage.person'
        db.delete_column(u'cv_foreignlanguage', 'person_id')

        # Adding field 'ForeignLanguage.user'
        db.add_column(u'cv_foreignlanguage', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Skills.person'
        db.delete_column(u'cv_skills', 'person_id')

        # Adding field 'Skills.user'
        db.add_column(u'cv_skills', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Experience.person'
        db.delete_column(u'cv_experience', 'person_id')

        # Adding field 'Experience.user'
        db.add_column(u'cv_experience', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Other.person'
        db.delete_column(u'cv_other', 'person_id')

        # Adding field 'Other.user'
        db.add_column(u'cv_other', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=-1, to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Education.person'
        db.delete_column(u'cv_education', 'person_id')

        # Adding field 'Education.user'
        db.add_column(u'cv_education', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Education.extra_activities'
        db.add_column(u'cv_education', 'extra_activities',
                      self.gf('django.db.models.fields.TextField')(default=-1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'EducationActivities'
        db.create_table(u'cv_educationactivities', (
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cv', ['EducationActivities'])

        # Adding field 'ForeignLanguage.person'
        db.add_column(u'cv_foreignlanguage', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'ForeignLanguage.user'
        db.delete_column(u'cv_foreignlanguage', 'user_id')

        # Adding field 'Skills.person'
        db.add_column(u'cv_skills', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Skills.user'
        db.delete_column(u'cv_skills', 'user_id')

        # Adding field 'Experience.person'
        db.add_column(u'cv_experience', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Experience.user'
        db.delete_column(u'cv_experience', 'user_id')

        # Adding field 'Other.person'
        db.add_column(u'cv_other', 'person',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=-1, to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Deleting field 'Other.user'
        db.delete_column(u'cv_other', 'user_id')

        # Adding field 'Education.person'
        db.add_column(u'cv_education', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Education.user'
        db.delete_column(u'cv_education', 'user_id')

        # Deleting field 'Education.extra_activities'
        db.delete_column(u'cv_education', 'extra_activities')


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
            'extra_activities': ('django.db.models.fields.TextField', [], {}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'start_date': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cv.experience': {
            'Meta': {'object_name': 'Experience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cv.foreignlanguage': {
            'Meta': {'object_name': 'ForeignLanguage'},
            'extra_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'reading': ('django.db.models.fields.IntegerField', [], {}),
            'speaking': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cv.other': {
            'Meta': {'object_name': 'Other'},
            'about_yourself': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expectations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefered_job': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'cv.skills': {
            'Meta': {'object_name': 'Skills'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'cv.userdetail': {
            'Meta': {'object_name': 'UserDetail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'web_page': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['cv']