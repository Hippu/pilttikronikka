# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.tutor'
        db.add_column(u'kronikka_student', 'tutor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['kronikka.Tutor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.tutor'
        db.delete_column(u'kronikka_student', 'tutor_id')


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
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kronikka.Tutor']"})
        },
        u'kronikka.tutor': {
            'Meta': {'object_name': 'Tutor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['kronikka']