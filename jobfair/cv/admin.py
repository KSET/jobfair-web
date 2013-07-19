from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('access_code',)

admin.site.register(Person, PersonAdmin)
