from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from sorl.thumbnail.admin import AdminImageMixin

from flexslider.models import Slider, Slide


class SlideInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = Slide
    extra = 1
    max_num = 5
    
    
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'geometry')
    fieldsets = (
            (None, {
                'fields': ('name', ('width', 'height'), 'slideshowSpeed', 'slideshow')
            }),
            (_('Animation options'), {
                'classes': ('collapse',),
                'fields': (('animation', 'animationDuration', 'slideDirection'),)
            }),            
            (_('Advanced options'), {
                'classes': ('collapse',),
                'fields': ('directionNav', 'controlNav', 'keyboardNav', 'mousewheel', 'pausePlay', 'randomize', 
                           'animationLoop', 'pauseOnAction', 'pauseOnHover')
            }),
    )    
    inlines = [SlideInlineAdmin]
admin.site.register(Slider, SliderAdmin)
