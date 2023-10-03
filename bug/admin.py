from django.contrib import admin
from bug.models import Bug
# Register your models here.
class BugAdmin(admin.ModelAdmin):
    list_display = ('bug_description','bug_type','report_date','status')



admin.site.register(Bug,BugAdmin)
    