# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'kronikka_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'kronikka', ['Student'])

        # Adding model 'Tutor'
        db.create_table(u'kronikka_tutor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'kronikka', ['Tutor'])

        # Adding model 'Story'
        db.create_table(u'kronikka_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kronikka.Student'])),
            ('story', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'kronikka', ['Story'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'kronikka_student')

        # Deleting model 'Tutor'
        db.delete_table(u'kronikka_tutor')

        # Deleting model 'Story'
        db.delete_table(u'kronikka_story')


    models = {
        u'kronikka.story': {
            'Meta': {'object_name': 'Story'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.TextField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kronikka.Student']"})
        },
        u'kronikka.student': {
            'Meta': {'object_name': 'Student'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'kronikka.tutor': {
            'Meta': {'object_name': 'Tutor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['kronikka']