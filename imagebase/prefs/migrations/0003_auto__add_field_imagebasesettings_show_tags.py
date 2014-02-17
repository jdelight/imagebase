# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ImagebaseSettings.show_tags'
        db.add_column(u'prefs_imagebasesettings', 'show_tags',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ImagebaseSettings.show_tags'
        db.delete_column(u'prefs_imagebasesettings', 'show_tags')


    models = {
        u'prefs.imagebasesettings': {
            'Meta': {'object_name': 'ImagebaseSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_id': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['prefs']