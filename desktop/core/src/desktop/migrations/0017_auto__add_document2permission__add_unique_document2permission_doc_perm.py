# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document2Permission'
        db.create_table(u'desktop_document2permission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['desktop.Document2'])),
            ('all', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('perms', self.gf('django.db.models.fields.CharField')(default='read', max_length=10, db_index=True)),
            ('link', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255)),
        ))
        db.send_create_signal(u'desktop', ['Document2Permission'])

        # Adding M2M table for field users on 'Document2Permission'
        m2m_table_name = 'documentpermission2_users'
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document2permission', models.ForeignKey(orm[u'desktop.document2permission'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['document2permission_id', 'user_id'])

        # Adding M2M table for field groups on 'Document2Permission'
        m2m_table_name = 'documentpermission2_groups'
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document2permission', models.ForeignKey(orm[u'desktop.document2permission'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['document2permission_id', 'group_id'])

        # Adding unique constraint on 'Document2Permission', fields ['doc', 'perms']
        db.create_unique(u'desktop_document2permission', ['doc_id', 'perms'])


    def backwards(self, orm):
        # Removing unique constraint on 'Document2Permission', fields ['doc', 'perms']
        db.delete_unique(u'desktop_document2permission', ['doc_id', 'perms'])

        # Deleting model 'Document2Permission'
        db.delete_table(u'desktop_document2permission')

        # Removing M2M table for field users on 'Document2Permission'
        db.delete_table('documentpermission2_users')

        # Removing M2M table for field groups on 'Document2Permission'
        db.delete_table('documentpermission2_groups')


    models = {
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'desktop.document': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Document'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'extra': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'doc_owner'", 'to': u"orm['auth.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['desktop.DocumentTag']", 'db_index': 'True', 'symmetrical': 'False'}),
            'version': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'})
        },
        u'desktop.document2': {
            'Meta': {'ordering': "['-last_modified']", 'unique_together': "(('uuid', 'version', 'is_history'),)", 'object_name': 'Document2'},
            'data': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'dependencies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dependencies_rel_+'", 'db_index': 'True', 'to': u"orm['desktop.Document2']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'extra': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_history': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'doc2_owner'", 'to': u"orm['auth.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags_rel_+'", 'db_index': 'True', 'to': u"orm['desktop.Document2']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'05771f47-4dee-49fe-873c-864b43722e64'", 'max_length': '36', 'db_index': 'True'}),
            'version': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'db_index': 'True'})
        },
        u'desktop.document2permission': {
            'Meta': {'unique_together': "(('doc', 'perms'),)", 'object_name': 'Document2Permission'},
            'all': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'doc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['desktop.Document2']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'to': u"orm['auth.Group']", 'db_table': "'documentpermission2_groups'", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'perms': ('django.db.models.fields.CharField', [], {'default': "'read'", 'max_length': '10', 'db_index': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'to': u"orm['auth.User']", 'db_table': "'documentpermission2_users'", 'symmetrical': 'False'})
        },
        u'desktop.documentpermission': {
            'Meta': {'unique_together': "(('doc', 'perms'),)", 'object_name': 'DocumentPermission'},
            'doc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['desktop.Document']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'to': u"orm['auth.Group']", 'db_table': "'documentpermission_groups'", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perms': ('django.db.models.fields.CharField', [], {'default': "'read'", 'max_length': '10'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'to': u"orm['auth.User']", 'db_table': "'documentpermission_users'", 'symmetrical': 'False'})
        },
        u'desktop.documenttag': {
            'Meta': {'unique_together': "(('owner', 'tag'),)", 'object_name': 'DocumentTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'tag': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'desktop.settings': {
            'Meta': {'object_name': 'Settings'},
            'collect_usage': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tours_and_tutorials': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'})
        },
        u'desktop.userpreferences': {
            'Meta': {'object_name': 'UserPreferences'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.TextField', [], {'max_length': '4096'})
        }
    }

    complete_apps = ['desktop']