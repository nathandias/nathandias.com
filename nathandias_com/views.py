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


# Testing Email functionality
from django.core.mail import send_mail
from django.http import HttpResponse

def email_test(request):

    recipient = 'nathan@swingornothing.com'

    send_mail(
        "Test subject",
        'Testing, testing, 1.2.3',
        'admin@nathandias.com',
        [recipient],
        fail_silently=False,
    )
    return HttpResponse("I think I sent an email to %s" % recipient)
