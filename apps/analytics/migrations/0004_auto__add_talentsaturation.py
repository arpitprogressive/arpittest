# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TalentSaturation'
        db.create_table(u'analytics_talentsaturation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('headcount', self.gf('django.db.models.fields.IntegerField')()),
            ('attrition_pc', self.gf('django.db.models.fields.DecimalField')(default=5.0, max_digits=5, decimal_places=2)),
            ('cagr_pc', self.gf('django.db.models.fields.DecimalField')(default=8.6, max_digits=5, decimal_places=2)),
            ('fresher_hiring_pc', self.gf('django.db.models.fields.DecimalField')(default=95.0, max_digits=5, decimal_places=2)),
            ('need_for_experience_pc', self.gf('django.db.models.fields.DecimalField')(default=45.0, max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'analytics', ['TalentSaturation'])


    def backwards(self, orm):
        # Deleting model 'TalentSaturation'
        db.delete_table(u'analytics_talentsaturation')


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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'international': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'university_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
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
            'career_guide': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobility_map': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Sector']"})
        },
        'admin.track': {
            'Meta': {'object_name': 'Track'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'})
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
        u'analytics.diversityratiolevel': {
            'Meta': {'object_name': 'DiversityRatioLevel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_entry': ('django.db.models.fields.IntegerField', [], {}),
            'male_leadership': ('django.db.models.fields.IntegerField', [], {}),
            'male_middle': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'analytics.diversityratiosubsector': {
            'Meta': {'unique_together': "(('year', 'subsector'),)", 'object_name': 'DiversityRatioSubsector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.IntegerField', [], {}),
            'subsector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.genderdiversity': {
            'Meta': {'unique_together': "(('year', 'category'),)", 'object_name': 'GenderDiversity'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.itspend': {
            'Meta': {'unique_together': "(('year', 'sub_sector'),)", 'object_name': 'ITSpend'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'india_revenue': ('django.db.models.fields.IntegerField', [], {}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'world_spend': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.revenueoccupation': {
            'Meta': {'unique_together': "(('year', 'occupation'),)", 'object_name': 'RevenueOccupation'},
            'cagr_next_7_years': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Occupation']"}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.revenuesubsector': {
            'Meta': {'unique_together': "(('year', 'sub_sector'),)", 'object_name': 'RevenueSubsector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.revenuetotal': {
            'Meta': {'object_name': 'RevenueTotal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'most_likely_growth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'optimistic_growth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
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
        },
        u'analytics.talentsaturation': {
            'Meta': {'object_name': 'TalentSaturation'},
            'attrition_pc': ('django.db.models.fields.DecimalField', [], {'default': '5.0', 'max_digits': '5', 'decimal_places': '2'}),
            'cagr_pc': ('django.db.models.fields.DecimalField', [], {'default': '8.6', 'max_digits': '5', 'decimal_places': '2'}),
            'fresher_hiring_pc': ('django.db.models.fields.DecimalField', [], {'default': '95.0', 'max_digits': '5', 'decimal_places': '2'}),
            'headcount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need_for_experience_pc': ('django.db.models.fields.DecimalField', [], {'default': '45.0', 'max_digits': '5', 'decimal_places': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['analytics']