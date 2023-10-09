from django.contrib import admin
from .models import Bug

class BugAdmin(admin.ModelAdmin):
    list_display = ('bug_description','bug_type','report_date','status')

admin.site.register(Bug,BugAdmin)