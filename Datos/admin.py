from django.contrib import admin
from .models import Dato

class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('update',)
# Register your models here.
admin.site.register(Dato,RatingAdmin)