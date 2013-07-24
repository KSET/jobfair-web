from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse

import forms

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('cv:edit'))
    return HttpResponseRedirect(reverse('cv:new'))

def new(request):
    context = dict()
    userForm = forms.UserForm(request.POST or None)
    userDetailForm = forms.UserDetailForm(request.POST or None)
    educationForm = [forms.EducationForm(request.POST or None)]
    foreignLanguageFrom = [forms.ForeignLanguageForm(request.POST or None)]
    experienceForm = [forms.ExperienceForm(request.POST or None)]
    skillsForm = [forms.SkillsForm(request.POST or None)]
    otherForm = forms.OtherForm(request.POST or None)
    context['user_form'] = userForm
    context['user_detail_form'] = userDetailForm
    context['education_forms'] = educationForm
    context['foreign_language_forms'] = foreignLanguageFrom
    context['experience_forms'] = experienceForm
    context['skills_forms'] = skillsForm
    context['other_form'] = otherForm
    if userForm.is_valid() and userDetailForm.is_valid():
        new_user = userForm.save()
        new_user_detail = userDetailForm.save(commit=False)
        new_user_detail.user = new_user
        new_user_detail.save()
        context['message'] = 'Thank you, your input has been saved.'
    return render(request, 'cv/new.html', context)

def edit(request):
    if request.user.is_authenticated():
        return HttpResponse("Editing CV of a user {}, password {}".format(
            request.user.username, request.user.password))
    return HttpResponse("Need to log in")

