from django.views.generic.base import TemplateView

from flexslider.models import Slider

class TestView(TemplateView):

    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['slider_pk'] = Slider.objects.latest("pk").pk
        return context