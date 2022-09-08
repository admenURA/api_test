from django.contrib import admin

# Register your models here.

from .models import Clients, Mailing, Massege

admin.site.register(Clients)
admin.site.register(Mailing)
admin.site.register(Massege)