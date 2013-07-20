from django.forms import ModelForm

import models

class PersonForm(ModelForm):
    class Meta:
        model = models.Person


class PersonDetailForm(ModelForm):
    class Meta:
        model = models.PersonDetail


class EducationForm(ModelForm):
    class Meta:
        model = models.Education


class EducationActivitiesForm(ModelForm):
    class Meta:
        model = models.EducationActivities


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
