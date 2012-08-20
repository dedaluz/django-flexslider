from django import forms
from django.template import RequestContext
from django.template.loader import render_to_string, get_template_from_string

from contentmanager import registry
from contentmanager.plugins import BasePlugin

from flexslider.models import Slider


class SliderForm(forms.Form):
    slider = forms.ModelChoiceField(Slider.objects.all())


class Slider(BasePlugin):
    form = SliderForm
    verbose_name = 'Slider'
    verbose_name_plural = 'Slider'    

    def render(self, request):
        slider_id = self.params.get("slider", None)
        t = get_template_from_string("{% load slider %}{% slider slider_id %}")
        return t.render(RequestContext(request, {'slider_id': slider_id}))
    
registry.register(Slider)