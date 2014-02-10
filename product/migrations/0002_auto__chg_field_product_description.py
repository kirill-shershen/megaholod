# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.description'
        db.alter_column(u'product_product', 'description', self.gf('django.db.models.fields.TextField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'Product.description'
        db.alter_column(u'product_product', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        u'product.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['product']