from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import forms

def index(request):
    template = loader.get_template('cv/index.html')
    context = RequestContext(request, dict())
    return HttpResponse(template.render(context))

def new(request):
    form = forms.PersonForm()
    context = {'form': form}
    return render(request, 'cv/new.html', context)

def edit_profile(request, access_code="-1"):
    return HttpResponse("Editing CV with access code {}".format(access_code))

def edit_page(request):
    return HttpResponse("Enter your login info for profile editing")

