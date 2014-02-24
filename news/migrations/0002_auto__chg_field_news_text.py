# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'News.text'
        db.alter_column(u'news_news', 'text', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'News.text'
        db.alter_column(u'news_news', 'text', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        u'news.news': {
            'Meta': {'ordering': "['-time']", 'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['news']