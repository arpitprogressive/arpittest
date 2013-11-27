# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'account_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'account', ['UserProfile'])

        # Adding model 'StudentProfile'
        db.create_table(u'account_studentprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.UserProfile'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('address_line1', self.gf('django.db.models.fields.TextField')()),
            ('address_line2', self.gf('django.db.models.fields.TextField')()),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('educational_background', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('experience', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('key_skills', self.gf('django.db.models.fields.TextField')()),
            ('work_status', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('industry_belongs_to', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('functional_area', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('current_company', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'account', ['StudentProfile'])

        # Adding model 'EmailAddress'
        db.create_table(u'account_emailaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'account', ['EmailAddress'])

        # Adding model 'EmailConfirmation'
        db.create_table(u'account_emailconfirmation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.EmailAddress'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'account', ['EmailConfirmation'])

        # Adding model 'IndustryProfile'
        db.create_table(u'account_industryprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.UserProfile'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('est_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('industry_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sub_sector', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'account', ['IndustryProfile'])

        # Adding model 'TrainingProfile'
        db.create_table(u'account_trainingprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.UserProfile'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('est_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('area_of_specialization', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'account', ['TrainingProfile'])

        # Adding model 'GovernmentProfile'
        db.create_table(u'account_governmentprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['account.UserProfile'], unique=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('department_type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'account', ['GovernmentProfile'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'account_userprofile')

        # Deleting model 'StudentProfile'
        db.delete_table(u'account_studentprofile')

        # Deleting model 'EmailAddress'
        db.delete_table(u'account_emailaddress')

        # Deleting model 'EmailConfirmation'
        db.delete_table(u'account_emailconfirmation')

        # Deleting model 'IndustryProfile'
        db.delete_table(u'account_industryprofile')

        # Deleting model 'TrainingProfile'
        db.delete_table(u'account_trainingprofile')

        # Deleting model 'GovernmentProfile'
        db.delete_table(u'account_governmentprofile')


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
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'department_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'})
        },
        u'account.industryprofile': {
            'Meta': {'object_name': 'IndustryProfile'},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'est_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_sector': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'})
        },
        u'account.studentprofile': {
            'Meta': {'object_name': 'StudentProfile'},
            'address_line1': ('django.db.models.fields.TextField', [], {}),
            'address_line2': ('django.db.models.fields.TextField', [], {}),
            'current_company': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'educational_background': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'functional_area': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_belongs_to': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'key_skills': ('django.db.models.fields.TextField', [], {}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'}),
            'work_status': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'account.trainingprofile': {
            'Meta': {'object_name': 'TrainingProfile'},
            'area_of_specialization': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'est_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.UserProfile']", 'unique': 'True'})
        },
        u'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
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