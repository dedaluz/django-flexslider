from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail

from flexslider.models import Slider, Slide


class SlideInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Slide
    fields = ('position', 'image', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0
    
    
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fieldsets = (
            (_('Main'), {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('name', ('width', 'height'), 'slideshowSpeed', 'slideshow')
            }),
            (_('Animation options'), {
                'classes': ('grp-collapse grp-closed',),
                'fields': (('animation', 'animationDuration', 'slideDirection'),)
            }),            
            (_('Advanced options'), {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('directionNav', 'controlNav', 'keyboardNav', 'mousewheel', 'pausePlay', 'randomize', 
                           'animationLoop', 'pauseOnAction', 'pauseOnHover')
            }),
    )    
    inlines = [SlideInlineAdmin]
    
class SlideAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for Slide"""

    def thumbnail(self, obj):
           im = get_thumbnail(obj.image, '60x60', quality=99)
           return u"<img src='%s'>" % im.url
    thumbnail.allow_tags = True

    list_display = ('name', 'position', 'status', 'thumbnail',)
    list_display_links = ('name', 'thumbnail',)
    pass


admin.site.register(Slider, SliderAdmin)
admin.site.register(Slide, SlideAdmin)
