from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def members_list(request):
    templates = loader.get_template('members_list.html')
    mymembers = Member.objects.all().values()

    context = {
        'mymembers' : mymembers
    }

    return HttpResponse(templates.render(context, request))