from django.shortcuts import render
from django.views.generic.base import TemplateView

from developer_info.models import Testimonial, Project

class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):
    testimonials = Testimonial.objects.all()
    website_projects = Project.objects.all().filter(project_type__exact='w')
    code_projects = Project.objects.all().filter(project_type__exact='c')
    
    projects = Project.objects.all()

    context = {
        'testimonials' : testimonials,
        'website_projects' : website_projects,
        'code_projects' : code_projects,
    }
    return render(request, 'home.html', context=context)

def googleauth(request):
    authorization_code = request.GET.get('code', '')
    context = {
        'authorization_code' : authorization_code,
    }
    return render(request, 'googleauth.html', context=context)