from django.forms import ModelForm, ValidationError
from django.contrib.auth.models import User as AuthUser

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


class ForeignLanguageForm(ModelForm):
    class Meta:
        model = models.ForeignLanguage


class ExperienceForm(ModelForm):
    class Meta:
        model = models.Experience


class SkillsForm(ModelForm):
    class Meta:
        model = models.Skills


class OtherForm(ModelForm):
    class Meta:
        model = models.Other
