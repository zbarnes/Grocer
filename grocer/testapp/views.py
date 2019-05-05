from django.shortcuts import render
from django.views.generic.base import TemplateView
from testapp.models import Food_Requested, Organization

# Create your views here.

class HomeView(TemplateView):
    template_name = 'testapp/home.html'

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

class SignupView(TemplateView):
    template_name = 'testapp/signup/requester.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        context['tabs'] = [
            {
                'name': 'info',
                'title': 'Tell Us Who You Are!',
                'blurb': 'Thanks for joining Grocer! Your donations will help the needy and hungry.',
                'form' : 'rightForm'
            },
            {
                'name': 'organization',
                'title': 'Tell Us about your Organization and what you can offer',
                'blurb': 'Currently, only NGOs or other organizations can sign up.',
                'form' : 'business'
            }
        ]
        context['disclaimer'] = "You are protected by the Good Smaritan Law!"

        context['foods'] = Food_Requested.objects.all()

        return context


class DemoDash(TemplateView):
    template_name = 'testapp/demo_dash.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        context['rows'] = Organization.objects.all()
        context['disclaimer'] = "You are protected by the Good Smaritan Law!"

        context['foods'] = Food_Requested.objects.all()

        return context