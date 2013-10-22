# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Occupation'
        db.create_table(u'admin_occupation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, unique=True, max_length=9, db_index=True)),
            ('sub_sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.SubSector'])),
        ))
        db.send_create_signal('admin', ['Occupation'])

        # Deleting field 'OccupationalStandard.sector'
        db.delete_column(u'admin_occupationalstandard', 'sector_id')

        # Deleting field 'QualificationPack.sector'
        db.delete_column(u'admin_qualificationpack', 'sector_id')

        # Deleting field 'QualificationPack.sub_sector'
        db.delete_column(u'admin_qualificationpack', 'sub_sector_id')


        # Renaming column for 'QualificationPack.occupation' to match new field type.
        db.rename_column(u'admin_qualificationpack', 'occupation', 'occupation_id')
        # Changing field 'QualificationPack.occupation'
        db.alter_column(u'admin_qualificationpack', 'occupation_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Occupation']))

    def backwards(self, orm):
        # Deleting model 'Occupation'
        db.delete_table(u'admin_occupation')


        # User chose to not deal with backwards NULL issues for 'OccupationalStandard.sector'
        raise RuntimeError("Cannot reverse this migration. 'OccupationalStandard.sector' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'OccupationalStandard.sector'
        db.add_column(u'admin_occupationalstandard', 'sector',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Sector']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'QualificationPack.sector'
        raise RuntimeError("Cannot reverse this migration. 'QualificationPack.sector' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'QualificationPack.sector'
        db.add_column(u'admin_qualificationpack', 'sector',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Sector']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'QualificationPack.sub_sector'
        raise RuntimeError("Cannot reverse this migration. 'QualificationPack.sub_sector' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'QualificationPack.sub_sector'
        db.add_column(u'admin_qualificationpack', 'sub_sector',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.SubSector']),
                      keep_default=False)


        # Renaming column for 'QualificationPack.occupation' to match new field type.
        db.rename_column(u'admin_qualificationpack', 'occupation_id', 'occupation')
        # Changing field 'QualificationPack.occupation'
        db.alter_column(u'admin_qualificationpack', 'occupation', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        'admin.company': {
            'Meta': {'object_name': 'Company'},
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
        u'admin.logentry': {
            'Meta': {'ordering': "(u'-action_time',)", 'object_name': 'LogEntry', 'db_table': "u'django_admin_log'"},
            'action_flag': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'change_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'admin.occupation': {
            'Meta': {'object_name': 'Occupation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'unique': 'True', 'max_length': '9', 'db_index': 'True'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"})
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
        'admin.qualificationpack': {
            'Meta': {'unique_together': "(('code', 'version'),)", 'object_name': 'QualificationPack'},
            'alias': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '9', 'db_index': 'True'}),
            'drafted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'job_role': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'last_reviewed_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'max_educational_qualification': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'min_educational_qualification': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'next_review_on': ('django.db.models.fields.DateField', [], {}),
            'nveqf_level': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '5'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['admin.Occupation']"}),
            'os_compulsory': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'os_compulsory'", 'symmetrical': 'False', 'to': "orm['admin.OccupationalStandard']"}),
            'os_optional': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'os_optional'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['admin.OccupationalStandard']"}),
            'role_description': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'training': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '8', 'db_index': 'True'})
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

    complete_apps = ['admin']