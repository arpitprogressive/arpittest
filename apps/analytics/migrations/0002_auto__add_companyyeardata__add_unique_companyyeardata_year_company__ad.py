# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompanyYearData'
        db.create_table(u'analytics_companyyeardata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Company'])),
            ('revenue', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'analytics', ['CompanyYearData'])

        # Adding unique constraint on 'CompanyYearData', fields ['year', 'company']
        db.create_unique(u'analytics_companyyeardata', ['year', 'company_id'])

        # Adding field 'DemandData.headcount'
        db.add_column(u'analytics_demanddata', 'headcount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'CompanyYearData', fields ['year', 'company']
        db.delete_unique(u'analytics_companyyeardata', ['year', 'company_id'])

        # Deleting model 'CompanyYearData'
        db.delete_table(u'analytics_companyyeardata')

        # Deleting field 'DemandData.headcount'
        db.delete_column(u'analytics_demanddata', 'headcount')


    models = {
        'admin.company': {
            'Meta': {'object_name': 'Company'},
            'company_type': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'nasscom_membership_number': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '20'}),
            'training_provider': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '3'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '100'})
        },
        'admin.institution': {
            'Meta': {'object_name': 'Institution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'international': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '100'})
        },
        'admin.occupation': {
            'Meta': {'object_name': 'Occupation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['admin.Track']", 'null': 'True', 'blank': 'True'})
        },
        'admin.sector': {
            'Meta': {'object_name': 'Sector', 'index_together': "[['name']]"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '9', 'db_index': 'True'})
        },
        'admin.subsector': {
            'Meta': {'unique_together': "(('sector', 'name'),)", 'object_name': 'SubSector', 'index_together': "[['name', 'sector']]"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Sector']"})
        },
        'admin.track': {
            'Meta': {'object_name': 'Track'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        u'analytics.city': {
            'Meta': {'unique_together': "(('name', 'state'),)", 'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.State']"})
        },
        u'analytics.companyyeardata': {
            'Meta': {'unique_together': "(('year', 'company'),)", 'object_name': 'CompanyYearData'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.demanddata': {
            'Meta': {'unique_together': "(('year', 'city', 'occupation', 'company'),)", 'object_name': 'DemandData'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Company']"}),
            'demand': ('django.db.models.fields.IntegerField', [], {}),
            'headcount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Occupation']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.state': {
            'Meta': {'unique_together': "(('name', 'region'),)", 'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'analytics.supplybase': {
            'Meta': {'unique_together': "(('year', 'city', 'occupation', 'institution', 'degree'),)", 'object_name': 'SupplyBase'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']"}),
            'degree': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Institution']"}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Occupation']"}),
            'supply': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['analytics']