import os

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.core.cache import cache
from django.template.defaultfilters import slugify
from django.utils.translation import string_concat
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail import ImageField

from managers import PublicManager


def slider_upload_path(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join("flexslider", str(instance.slider.pk), slugify(filename) + ext)


class Slider(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)
    width = models.PositiveSmallIntegerField(_("width"))
    height = models.PositiveSmallIntegerField(_("height"))
    # configuration options
    ANIMATION_CHOICES = (
        (u"fade", _(u"fade")),
        (u"slide", _(u"slide"))
    )
    animation = models.CharField(_("animation"), max_length=25,
                                 choices=ANIMATION_CHOICES, default="fade")
    SLIDE_CHOICES = (
        (u"horizontal", _(u"horizontal")),
        (u"vertical", _(u"vertical"))
    )    
    slideDirection = models.CharField(_("slide direction"), max_length=25,
                                      choices=SLIDE_CHOICES, default="horizontal")
    slideshow = models.BooleanField(_("animate slider automatically"), default=True)
    slideshowSpeed = models.PositiveIntegerField(_("cycle speed"), default=7000, 
                                                 help_text=_("Set the speed of the slideshow cycling, in milliseconds"))
    animationDuration = models.PositiveIntegerField(_("animation duration"), default=600,
                                                    help_text=_("Set the speed of animations, in milliseconds"))
    directionNav = models.BooleanField(_("Create navigation for previous/next navigation?"), default=True)
    controlNav = models.BooleanField(_("Create navigation for paging control of each slide?"), default=True)
    keyboardNav = models.BooleanField(_("Allow slider navigating via keyboard left/right keys"), default=True)
    mousewheel = models.BooleanField(_("Allow slider navigating via mousewheel"), default=False)
    pausePlay = models.BooleanField(_("Create pause/play dynamic element"), default=False)
    randomize = models.BooleanField(_("Randomize slide order"), default=False)
    animationLoop = models.BooleanField(_("Should the animation loop?"), default=True)
    pauseOnAction = models.BooleanField(_("Pause the slideshow when interacting with control elements, highly recommended."), default=True)
    pauseOnHover = models.BooleanField(_("Pause the slideshow when hovering over slider"), default=False)
    
    def __unicode__(self):
        return self.name
    
    @classmethod
    def get_cache_key_for(self, pk):
        return u"flexslider:%d" % pk
    
    def get_cache_key(self):
        return Slider.get_cache_key_for(self.pk)
    
    def geometry(self):
        return u"%dx%d" % (self.width, self.height)
    
    def settings(self):
        lst = [
            string_concat(u"prevText: '", _("Previous"), "'"),
            string_concat(u"nextText: '", _("Next"), "'"),
            string_concat(u"pauseText: '", _('Pause'), "'"),
            string_concat(u"playText: '", _('Play'), "'"),
            "animation: '%s'" % self.animation,
            "slideDirection: '%s'" % self.slideDirection,
            "slideshow: %s" % str(self.slideshow).lower(),
            "slideshowSpeed: %d" % self.slideshowSpeed,
            "animationDuration: %d" % self.animationDuration,
            "directionNav: %s" % str(self.directionNav).lower(),
            "controlNav: %s" % str(self.controlNav).lower(),
            "keyboardNav: %s" % str(self.keyboardNav).lower(), 
            "mousewheel: %s" % str(self.mousewheel).lower(),
            "pausePlay: %s" % str(self.pausePlay).lower(),
            "randomize: %s" % str(self.randomize).lower(),
            "animationLoop: %s" % str(self.animationLoop).lower(), 
            "pauseOnAction: %s" % str(self.pauseOnAction).lower(),
            "pauseOnHover: %s" % str(self.pauseOnHover).lower()         
        ]
        return lst
    
    
class Slide(models.Model):
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
    )
    
    name = models.CharField(max_length=150, blank=True)
    slider = models.ForeignKey(Slider, related_name="slides")
    image = ImageField(_("image"), max_length=250, upload_to=slider_upload_path)
    link = models.URLField(_("link"), max_length=250, blank=True, verify_exists=False)
    caption = models.TextField(_("caption"), blank=True)
    description = models.TextField(_('description'), blank=True)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    credit = models.TextField(_("credit"), blank=True)
    # position field
    position = models.PositiveSmallIntegerField("Position", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name = u'Slide'
        verbose_name_plural = 'Slides'
        ordering = ('position',)

# cache busting when saving or deleting.
def cache_buster(sender, **kwargs):
    instance = kwargs.pop("instance")
    if instance:
        if sender == Slide:
            cache.delete(instance.slider.get_cache_key())
        else:
            cache.delete(instance.get_cache_key())
    
post_save.connect(cache_buster, sender=Slider, dispatch_uid="cache_buster_slider_save")
pre_delete.connect(cache_buster, sender=Slider, dispatch_uid="cache_buster_slider_delete")
post_save.connect(cache_buster, sender=Slide, dispatch_uid="cache_buster_slide_save")
pre_delete.connect(cache_buster, sender=Slide, dispatch_uid="cache_buster_slide_delete")