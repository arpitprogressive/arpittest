# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'State.create_date'
        db.add_column(u'analytics_state', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'State.write_date'
        db.add_column(u'analytics_state', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'GenderDiversity.create_date'
        db.add_column(u'analytics_genderdiversity', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'GenderDiversity.write_date'
        db.add_column(u'analytics_genderdiversity', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RevenueOccupation.create_date'
        db.add_column(u'analytics_revenueoccupation', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RevenueOccupation.write_date'
        db.add_column(u'analytics_revenueoccupation', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SupplyBase.create_date'
        db.add_column(u'analytics_supplybase', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'SupplyBase.write_date'
        db.add_column(u'analytics_supplybase', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'ITSpend.create_date'
        db.add_column(u'analytics_itspend', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'ITSpend.write_date'
        db.add_column(u'analytics_itspend', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DiversityRatioLevel.create_date'
        db.add_column(u'analytics_diversityratiolevel', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DiversityRatioLevel.write_date'
        db.add_column(u'analytics_diversityratiolevel', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RevenueSubsector.create_date'
        db.add_column(u'analytics_revenuesubsector', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RevenueSubsector.write_date'
        db.add_column(u'analytics_revenuesubsector', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DiversityRatioSubsector.create_date'
        db.add_column(u'analytics_diversityratiosubsector', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DiversityRatioSubsector.write_date'
        db.add_column(u'analytics_diversityratiosubsector', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'City.create_date'
        db.add_column(u'analytics_city', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'City.write_date'
        db.add_column(u'analytics_city', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'CompanyYearData.create_date'
        db.add_column(u'analytics_companyyeardata', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'CompanyYearData.write_date'
        db.add_column(u'analytics_companyyeardata', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RevenueTotal.create_date'
        db.add_column(u'analytics_revenuetotal', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'RevenueTotal.write_date'
        db.add_column(u'analytics_revenuetotal', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'TalentSaturation.create_date'
        db.add_column(u'analytics_talentsaturation', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'TalentSaturation.write_date'
        db.add_column(u'analytics_talentsaturation', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DemandData.create_date'
        db.add_column(u'analytics_demanddata', 'create_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DemandData.write_date'
        db.add_column(u'analytics_demanddata', 'write_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 31, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'State.create_date'
        db.delete_column(u'analytics_state', 'create_date')

        # Deleting field 'State.write_date'
        db.delete_column(u'analytics_state', 'write_date')

        # Deleting field 'GenderDiversity.create_date'
        db.delete_column(u'analytics_genderdiversity', 'create_date')

        # Deleting field 'GenderDiversity.write_date'
        db.delete_column(u'analytics_genderdiversity', 'write_date')

        # Deleting field 'RevenueOccupation.create_date'
        db.delete_column(u'analytics_revenueoccupation', 'create_date')

        # Deleting field 'RevenueOccupation.write_date'
        db.delete_column(u'analytics_revenueoccupation', 'write_date')

        # Deleting field 'SupplyBase.create_date'
        db.delete_column(u'analytics_supplybase', 'create_date')

        # Deleting field 'SupplyBase.write_date'
        db.delete_column(u'analytics_supplybase', 'write_date')

        # Deleting field 'ITSpend.create_date'
        db.delete_column(u'analytics_itspend', 'create_date')

        # Deleting field 'ITSpend.write_date'
        db.delete_column(u'analytics_itspend', 'write_date')

        # Deleting field 'DiversityRatioLevel.create_date'
        db.delete_column(u'analytics_diversityratiolevel', 'create_date')

        # Deleting field 'DiversityRatioLevel.write_date'
        db.delete_column(u'analytics_diversityratiolevel', 'write_date')

        # Deleting field 'RevenueSubsector.create_date'
        db.delete_column(u'analytics_revenuesubsector', 'create_date')

        # Deleting field 'RevenueSubsector.write_date'
        db.delete_column(u'analytics_revenuesubsector', 'write_date')

        # Deleting field 'DiversityRatioSubsector.create_date'
        db.delete_column(u'analytics_diversityratiosubsector', 'create_date')

        # Deleting field 'DiversityRatioSubsector.write_date'
        db.delete_column(u'analytics_diversityratiosubsector', 'write_date')

        # Deleting field 'City.create_date'
        db.delete_column(u'analytics_city', 'create_date')

        # Deleting field 'City.write_date'
        db.delete_column(u'analytics_city', 'write_date')

        # Deleting field 'CompanyYearData.create_date'
        db.delete_column(u'analytics_companyyeardata', 'create_date')

        # Deleting field 'CompanyYearData.write_date'
        db.delete_column(u'analytics_companyyeardata', 'write_date')

        # Deleting field 'RevenueTotal.create_date'
        db.delete_column(u'analytics_revenuetotal', 'create_date')

        # Deleting field 'RevenueTotal.write_date'
        db.delete_column(u'analytics_revenuetotal', 'write_date')

        # Deleting field 'TalentSaturation.create_date'
        db.delete_column(u'analytics_talentsaturation', 'create_date')

        # Deleting field 'TalentSaturation.write_date'
        db.delete_column(u'analytics_talentsaturation', 'write_date')

        # Deleting field 'DemandData.create_date'
        db.delete_column(u'analytics_demanddata', 'create_date')

        # Deleting field 'DemandData.write_date'
        db.delete_column(u'analytics_demanddata', 'write_date')


    models = {
        'admin.company': {
            'Meta': {'object_name': 'Company'},
            'company_type': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'nasscom_membership_number': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '20'}),
            'training_provider': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '3'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '100'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.institution': {
            'Meta': {'object_name': 'Institution'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']", 'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'international': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'university_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '100'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.occupation': {
            'Meta': {'object_name': 'Occupation'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'tracks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['admin.Track']", 'null': 'True', 'blank': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.sector': {
            'Meta': {'object_name': 'Sector', 'index_together': "[['name']]"},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '9', 'db_index': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.subsector': {
            'Meta': {'unique_together': "(('sector', 'name'),)", 'object_name': 'SubSector', 'index_together': "[['name', 'sector']]"},
            'career_guide': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobility_map': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Sector']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'admin.track': {
            'Meta': {'object_name': 'Track'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'analytics.city': {
            'Meta': {'unique_together': "(('name', 'state'),)", 'object_name': 'City'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.State']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'analytics.companyyeardata': {
            'Meta': {'unique_together': "(('year', 'company'),)", 'object_name': 'CompanyYearData'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Company']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.demanddata': {
            'Meta': {'unique_together': "(('year', 'city', 'occupation', 'company'),)", 'object_name': 'DemandData'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Company']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'demand': ('django.db.models.fields.IntegerField', [], {}),
            'headcount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Occupation']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.diversityratiolevel': {
            'Meta': {'object_name': 'DiversityRatioLevel'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male_entry': ('django.db.models.fields.IntegerField', [], {}),
            'male_leadership': ('django.db.models.fields.IntegerField', [], {}),
            'male_middle': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'analytics.diversityratiosubsector': {
            'Meta': {'unique_together': "(('year', 'subsector'),)", 'object_name': 'DiversityRatioSubsector'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.IntegerField', [], {}),
            'subsector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.genderdiversity': {
            'Meta': {'unique_together': "(('year', 'category'),)", 'object_name': 'GenderDiversity'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'male': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.itspend': {
            'Meta': {'unique_together': "(('year', 'sub_sector'),)", 'object_name': 'ITSpend'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'india_revenue': ('django.db.models.fields.IntegerField', [], {}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'world_spend': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.revenueoccupation': {
            'Meta': {'unique_together': "(('year', 'occupation'),)", 'object_name': 'RevenueOccupation'},
            'cagr_next_7_years': ('django.db.models.fields.IntegerField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Occupation']"}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.revenuesubsector': {
            'Meta': {'unique_together': "(('year', 'sub_sector'),)", 'object_name': 'RevenueSubsector'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.revenuetotal': {
            'Meta': {'object_name': 'RevenueTotal'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'most_likely_growth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'optimistic_growth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'analytics.state': {
            'Meta': {'unique_together': "(('name', 'region'),)", 'object_name': 'State'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '50'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'analytics.supplybase': {
            'Meta': {'unique_together': "(('year', 'city', 'occupation', 'institution', 'degree'),)", 'object_name': 'SupplyBase'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analytics.City']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Institution']"}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Occupation']"}),
            'supply': ('django.db.models.fields.IntegerField', [], {}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analytics.talentsaturation': {
            'Meta': {'object_name': 'TalentSaturation'},
            'attrition_pc': ('django.db.models.fields.DecimalField', [], {'default': '5.0', 'max_digits': '5', 'decimal_places': '2'}),
            'cagr_pc': ('django.db.models.fields.DecimalField', [], {'default': '8.6', 'max_digits': '5', 'decimal_places': '2'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fresher_hiring_pc': ('django.db.models.fields.DecimalField', [], {'default': '95.0', 'max_digits': '5', 'decimal_places': '2'}),
            'headcount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need_for_experience_pc': ('django.db.models.fields.DecimalField', [], {'default': '45.0', 'max_digits': '5', 'decimal_places': '2'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['analytics']