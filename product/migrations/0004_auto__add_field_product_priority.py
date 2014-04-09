# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.priority'
        db.add_column(u'product_product', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.priority'
        db.delete_column(u'product_product', 'priority')


    models = {
        u'product.object': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Object'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'product.product': {
            'Meta': {'ordering': "['category', 'name']", 'object_name': 'Product'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '100'})
        }
    }

    complete_apps = ['product']