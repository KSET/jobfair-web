from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import forms

def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('cv:edit'))
    return redirect(reverse('cv:new'))

def new(request):
    userForm = forms.UserForm(request.POST or None)
    userDetailForm = forms.UserDetailForm(request.POST or None)
    educationFormSet = forms.educationFormSet(request.POST or None)
    foreignLanguageFormSet = forms.foreignLanguageFormSet(
            request.POST or None)
    experienceFormSet = forms.experienceFormSet(request.POST or None)
    skillsFormSet = forms.skillsFormSet(request.POST or None)
    otherForm = forms.OtherForm(request.POST or None)
    context = {'user_form': userForm,
            'user_detail_form': userDetailForm,
            'education_formset': educationFormSet,
            'foreign_language_formset': foreignLanguageFormSet,
            'experience_formset': experienceFormSet,
            'skills_formset': skillsFormSet,
            'other_form': otherForm,
            }
    valid_list = [x.is_valid() for x in  context.itervalues()]
    if all(valid_list):
        user = userForm.save()
        user_detail = userDetailForm.save(commit=False)
        user_detail.user = user
        user_detail.save()
        for form in educationFormSet:
            education = form.save(commit=False)
            education.user = user
            education.save()

        context['message'] = 'Thank you, your input has been saved.'
    return render(request, 'cv/new.html', context)

@login_required(login_url='/cv/login')
def edit(request):
    return HttpResponse("Editing CV of a user {}".format(
        request.user.username))

