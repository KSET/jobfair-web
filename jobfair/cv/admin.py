from django.contrib import admin
from django.db.models import get_models, get_app
from django.contrib.admin.sites import AlreadyRegistered
import models

def autoregister(app):
    current_app = get_app(app)
    for model in get_models(current_app):
        try:
            admin.site.register(model)
        except AlreadyRegistered:
            pass

autoregister('cv')
