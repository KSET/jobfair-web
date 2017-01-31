from django.forms import ModelForm, ValidationError
from django.contrib.auth.models import User as AuthUser
from django.forms.formsets import formset_factory, BaseFormSet

import models

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email')


class UserDetailForm(ModelForm):
    class Meta:
        model = models.UserDetail
        exclude = ('user',)


class EducationForm(ModelForm):
    class Meta:
        model = models.Education
        exclude = ('user',)


class ForeignLanguageForm(ModelForm):
    class Meta:
        model = models.ForeignLanguage
        exclude = ('user',)


class ExperienceForm(ModelForm):
    class Meta:
        model = models.Experience
        exclude = ('user',)


class SkillsForm(ModelForm):
    class Meta:
        model = models.Skills
        exclude = ('user',)


class OtherForm(ModelForm):
    class Meta:
        model = models.Other
        exclude = ('user',)


educationFormSet = formset_factory(EducationForm, max_num=10)
foreignLanguageFormSet = formset_factory(ForeignLanguageForm, max_num=10)
experienceFormSet = formset_factory(ExperienceForm, max_num=10)
skillsFormSet = formset_factory(SkillsForm, max_num=30)

