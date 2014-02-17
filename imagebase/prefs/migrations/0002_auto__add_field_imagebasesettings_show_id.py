# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ImagebaseSettings.show_id'
        db.add_column(u'prefs_imagebasesettings', 'show_id',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ImagebaseSettings.show_id'
        db.delete_column(u'prefs_imagebasesettings', 'show_id')


    models = {
        u'prefs.imagebasesettings': {
            'Meta': {'object_name': 'ImagebaseSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_id': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['prefs']