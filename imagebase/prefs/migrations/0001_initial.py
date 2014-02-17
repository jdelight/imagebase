# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImagebaseSettings'
        db.create_table(u'prefs_imagebasesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('show_title', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'prefs', ['ImagebaseSettings'])


    def backwards(self, orm):
        # Deleting model 'ImagebaseSettings'
        db.delete_table(u'prefs_imagebasesettings')


    models = {
        u'prefs.imagebasesettings': {
            'Meta': {'object_name': 'ImagebaseSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['prefs']