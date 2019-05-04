from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class DemoView(TemplateView):
    template_name = "testapp/test.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        context['tabs'] = [
            {
                'name': 'Example',
                'blurb': 'ahhhh'
            },
            {
                'name': 'Example2',
            }
        ]
        context['note'] = "You are protected by the Good Smaritan Law!"

        return context
