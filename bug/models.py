from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Bug(models.Model):
    
    # Tuple for bug_types
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
    
    # string representation
    def __str__(self):
        return f"{self.bug_description} ({self.bug_type} - Reported on {self.report_date.strftime('%b. %d, %Y')})"
    
    def was_published_recently(self):        
        now = timezone.now().date()
        return now - datetime.timedelta(days=1) <= self.report_date <= now