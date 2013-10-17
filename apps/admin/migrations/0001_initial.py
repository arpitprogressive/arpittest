# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sector'
        db.create_table(u'admin_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, unique=True, max_length=9, db_index=True)),
        ))
        db.send_create_signal('admin', ['Sector'])

        # Adding index on 'Sector', fields ['name']
        db.create_index(u'admin_sector', ['name'])

        # Adding model 'SubSector'
        db.create_table(u'admin_subsector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Sector'])),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, db_index=True)),
        ))
        db.send_create_signal('admin', ['SubSector'])

        # Adding unique constraint on 'SubSector', fields ['sector', 'name']
        db.create_unique(u'admin_subsector', ['sector_id', 'name'])

        # Adding index on 'SubSector', fields ['name', 'sector']
        db.create_index(u'admin_subsector', ['name', 'sector_id'])

        # Adding model 'OccupationalStandard'
        db.create_table(u'admin_occupationalstandard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(default=None, max_length=9, db_index=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default=None, max_length=8, db_index=True)),
            ('is_draft', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Sector'])),
            ('sub_sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.SubSector'])),
            ('title', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default=None)),
            ('scope', self.gf('tinymce.models.HTMLField')(default=None)),
            ('performace_criteria', self.gf('tinymce.models.HTMLField')(default=None)),
            ('knowledge', self.gf('tinymce.models.HTMLField')(default=None)),
            ('skills', self.gf('tinymce.models.HTMLField')(default=None)),
            ('drafted_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_reviewed_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('next_review_on', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('admin', ['OccupationalStandard'])

        # Adding unique constraint on 'OccupationalStandard', fields ['code', 'version']
        db.create_unique(u'admin_occupationalstandard', ['code', 'version'])

        # Adding model 'QualificationPack'
        db.create_table(u'admin_qualificationpack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(default=None, max_length=9, db_index=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default=None, max_length=8, db_index=True)),
            ('is_draft', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.Sector'])),
            ('sub_sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['admin.SubSector'])),
            ('occupation', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, db_index=True)),
            ('job_role', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, db_index=True)),
            ('alias', self.gf('django.db.models.fields.TextField')(default=None)),
            ('role_description', self.gf('django.db.models.fields.TextField')(default=None)),
            ('nveqf_level', self.gf('django.db.models.fields.CharField')(default=None, max_length=5)),
            ('min_educational_qualification', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('max_educational_qualification', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('training', self.gf('django.db.models.fields.TextField')()),
            ('experience', self.gf('django.db.models.fields.TextField')(default=None)),
            ('drafted_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_reviewed_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('next_review_on', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('admin', ['QualificationPack'])

        # Adding unique constraint on 'QualificationPack', fields ['code', 'version']
        db.create_unique(u'admin_qualificationpack', ['code', 'version'])

        # Adding M2M table for field os_compulsory on 'QualificationPack'
        m2m_table_name = db.shorten_name(u'admin_qualificationpack_os_compulsory')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('qualificationpack', models.ForeignKey(orm['admin.qualificationpack'], null=False)),
            ('occupationalstandard', models.ForeignKey(orm['admin.occupationalstandard'], null=False))
        ))
        db.create_unique(m2m_table_name, ['qualificationpack_id', 'occupationalstandard_id'])

        # Adding M2M table for field os_optional on 'QualificationPack'
        m2m_table_name = db.shorten_name(u'admin_qualificationpack_os_optional')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('qualificationpack', models.ForeignKey(orm['admin.qualificationpack'], null=False)),
            ('occupationalstandard', models.ForeignKey(orm['admin.occupationalstandard'], null=False))
        ))
        db.create_unique(m2m_table_name, ['qualificationpack_id', 'occupationalstandard_id'])

        # Adding model 'Institution'
        db.create_table(u'admin_institution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, unique=True, max_length=100, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=100)),
            ('international', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('admin', ['Institution'])

        # Adding model 'Company'
        db.create_table(u'admin_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, unique=True, max_length=100, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=100)),
            ('nasscom_membership_number', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=20)),
            ('training_provider', self.gf('django.db.models.fields.CharField')(default='NO', max_length=3)),
        ))
        db.send_create_signal('admin', ['Company'])

        # Adding model 'LogEntry'
        db.create_table(u'django_admin_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('object_repr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('action_flag', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('change_message', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'admin', ['LogEntry'])


    def backwards(self, orm):
        # Removing unique constraint on 'QualificationPack', fields ['code', 'version']
        db.delete_unique(u'admin_qualificationpack', ['code', 'version'])

        # Removing unique constraint on 'OccupationalStandard', fields ['code', 'version']
        db.delete_unique(u'admin_occupationalstandard', ['code', 'version'])

        # Removing index on 'SubSector', fields ['name', 'sector']
        db.delete_index(u'admin_subsector', ['name', 'sector_id'])

        # Removing unique constraint on 'SubSector', fields ['sector', 'name']
        db.delete_unique(u'admin_subsector', ['sector_id', 'name'])

        # Removing index on 'Sector', fields ['name']
        db.delete_index(u'admin_sector', ['name'])

        # Deleting model 'Sector'
        db.delete_table(u'admin_sector')

        # Deleting model 'SubSector'
        db.delete_table(u'admin_subsector')

        # Deleting model 'OccupationalStandard'
        db.delete_table(u'admin_occupationalstandard')

        # Deleting model 'QualificationPack'
        db.delete_table(u'admin_qualificationpack')

        # Removing M2M table for field os_compulsory on 'QualificationPack'
        db.delete_table(db.shorten_name(u'admin_qualificationpack_os_compulsory'))

        # Removing M2M table for field os_optional on 'QualificationPack'
        db.delete_table(db.shorten_name(u'admin_qualificationpack_os_optional'))

        # Deleting model 'Institution'
        db.delete_table(u'admin_institution')

        # Deleting model 'Company'
        db.delete_table(u'admin_company')

        # Deleting model 'LogEntry'
        db.delete_table(u'django_admin_log')


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
        'admin.occupationalstandard': {
            'Meta': {'unique_together': "(('code', 'version'),)", 'object_name': 'OccupationalStandard'},
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
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Sector']"}),
            'skills': ('tinymce.models.HTMLField', [], {'default': 'None'}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '8', 'db_index': 'True'})
        },
        'admin.qualificationpack': {
            'Meta': {'unique_together': "(('code', 'version'),)", 'object_name': 'QualificationPack'},
            'alias': ('django.db.models.fields.TextField', [], {'default': 'None'}),
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
            'occupation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'db_index': 'True'}),
            'os_compulsory': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'os_compulsory'", 'symmetrical': 'False', 'to': "orm['admin.OccupationalStandard']"}),
            'os_optional': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'os_optional'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['admin.OccupationalStandard']"}),
            'role_description': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.Sector']"}),
            'sub_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['admin.SubSector']"}),
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