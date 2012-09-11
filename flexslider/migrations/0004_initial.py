# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table('flexslider_slider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('animation', self.gf('django.db.models.fields.CharField')(default='fade', max_length=25)),
            ('slideDirection', self.gf('django.db.models.fields.CharField')(default='horizontal', max_length=25)),
            ('slideshow', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('slideshowSpeed', self.gf('django.db.models.fields.PositiveIntegerField')(default=7000)),
            ('animationDuration', self.gf('django.db.models.fields.PositiveIntegerField')(default=600)),
            ('directionNav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('controlNav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('keyboardNav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mousewheel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pausePlay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('randomize', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('animationLoop', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pauseOnAction', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pauseOnHover', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('flexslider', ['Slider'])

        # Adding model 'Slide'
        db.create_table('flexslider_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['flexslider.Slider'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=250)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=250, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('credit', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('flexslider', ['Slide'])

    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table('flexslider_slider')

        # Deleting model 'Slide'
        db.delete_table('flexslider_slide')

    models = {
        'flexslider.slide': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Slide'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '250'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': "orm['flexslider.Slider']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'flexslider.slider': {
            'Meta': {'object_name': 'Slider'},
            'animation': ('django.db.models.fields.CharField', [], {'default': "'fade'", 'max_length': '25'}),
            'animationDuration': ('django.db.models.fields.PositiveIntegerField', [], {'default': '600'}),
            'animationLoop': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'controlNav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'directionNav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyboardNav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mousewheel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'pauseOnAction': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pauseOnHover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pausePlay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'randomize': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slideDirection': ('django.db.models.fields.CharField', [], {'default': "'horizontal'", 'max_length': '25'}),
            'slideshow': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slideshowSpeed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '7000'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['flexslider']