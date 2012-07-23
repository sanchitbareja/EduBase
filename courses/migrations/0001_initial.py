# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table('courses_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('course_start_date', self.gf('django.db.models.fields.DateField')()),
            ('course_end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('courses', ['Course'])

        # Adding model 'Assessment'
        db.create_table('courses_assessment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Course'])),
            ('assessment_type', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('courses', ['Assessment'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table('courses_course')

        # Deleting model 'Assessment'
        db.delete_table('courses_assessment')


    models = {
        'courses.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'assessment_type': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['courses.Course']"}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'course_end_date': ('django.db.models.fields.DateField', [], {}),
            'course_start_date': ('django.db.models.fields.DateField', [], {}),
            'course_title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['courses']