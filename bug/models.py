from django.db import models

# Create your models here.
class Bug(models.Model):

    #tuple for bug_types
    BUG_TYPES = (
        ('error', 'error'), 
        ('new feature','new feature'), 
        ('code','code'),
        ('enhancement','enhancement')
    )

    STATUS = (
        ('To do','To do'),
        ('In Progress','In Progress'),
        ('Done','Done')


    )

    bug_description = models.TextField()
    bug_type = models.CharField(max_length = 50, choices = BUG_TYPES)
    report_date = models.DateField()
    status = models.CharField(max_length = 50, choices = STATUS)