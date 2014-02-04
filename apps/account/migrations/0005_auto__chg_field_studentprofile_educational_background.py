# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StudentProfile.educational_background'
        db.alter_column(u'account_studentprofile', 'educational_background', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'StudentProfile.educational_background'
        db.alter_column(u'account_studentprofile', 'educational_background', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'account.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'account.emailconfirmation': {
            'Meta': {'object_name': 'EmailConfirmation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.EmailAddress']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'account.governmentprofile': {
            'Meta': {'object_name': 'GovernmentProfile'},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'department_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'account.industryprofile': {
            'Meta': {'object_name': 'IndustryProfile'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['admin.Company']", 'null': 'True', 'blank': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'est_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_sector': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'account.studentprofile': {
            'Meta': {'object_name': 'StudentProfile'},
            'address_line1': ('django.db.models.fields.TextField', [], {}),
            'address_line2': ('django.db.models.fields.TextField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_company': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'educational_background': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'functional_area': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_belongs_to': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'key_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['admin.OccupationalStandard']", 'symmetrical': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'}),
            'work_status': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'account.trainingprofile': {
            'Meta': {'object_name': 'TrainingProfile'},
            'area_of_specialization': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'est_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'write_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
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
        'admin.occupationalstandard': {
            'Meta': {'unique_together': "(('code', 'version'),)", 'object_name': 'OccupationalStandard'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '9', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'drafted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'knowledge': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'last_reviewed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'next_review_on': ('django.db.models.fields.DateField', [], {}),
            'performace_criteria': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'scope': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'skills': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '8', 'db_index': 'True'})
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
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['account']