from django import template
from django.core.cache import cache

from flexslider.models import Slider

register = template.Library()


@register.simple_tag
def slider(pk):
    ckey = Slider.get_cache_key_for(pk)
    result = cache.get(ckey)
    if result is None:
        # get slider
        try:
            slider = Slider.objects.get(pk=pk)
        except Slider.DoesNotExist:
            result = "Slider doesn't exist anymore."
        else:
            # actual rendering
            t = template.loader.select_template(["flexslider/slider_%d.html" % pk, "flexslider/slider.html"])
            result = t.render(template.Context({"slider": slider}))
        cache.set(ckey, result)
    return result
    
