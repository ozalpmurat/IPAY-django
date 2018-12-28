from django.contrib import admin

# Register your models here.
from .models import birim
admin.site.register(birim)
from .models import ip
admin.site.register(ip)
