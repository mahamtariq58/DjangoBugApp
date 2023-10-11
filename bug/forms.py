from django  import forms
from .models import Bug
from django.utils import timezone

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['bug_description', 'bug_type', 'report_date', 'status']
    def clean_report_date(self):
        report_date = self.cleaned_data['report_date']
        if report_date > timezone.now().date() or report_date < timezone.now().date():
            raise forms.ValidationError('Bug report date is not correct')
        return report_date

    def clean_bug_description(self):
        bug_description = self.cleaned_data['bug_description']
        existing_bug = Bug.objects.filter(bug_description=bug_description).first()
        if existing_bug:
            raise forms.ValidationError('Bug with this description already exists')
        return bug_description