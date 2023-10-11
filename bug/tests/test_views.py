from django.test import TestCase, Client
from django.urls import reverse
from ..models import Bug
import datetime 
from django.utils import timezone

# Test cases for views

class BugAppViewTests(TestCase):

    
    def setUp(self):

        # instance of client
        self.client = Client()
        self.valid_bug_data = {
            'bug_description': 'Valid Bug',
            'bug_type': 'error',
            'report_date': timezone.now().date(),
            'status': 'To do',
        }

  
    def test_no_question(self):
        """
        if no bug reported, an appropiate message is displayed.
        """ 
        response= self.client.get (reverse("bug:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No bugs are reported")
        self.assertQuerySetEqual(response.context["bugs"],[])

    def test_detail_view(self):
        
        self.sample_bug = Bug.objects.create(**self.valid_bug_data)
        response = self.client.get(reverse('bug:detail', args=[self.sample_bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.sample_bug.bug_description)
        self.assertContains(response, self.sample_bug.bug_type)
        self.assertContains(response, self.sample_bug.report_date.strftime('%b. %-d, %Y'))
        self.assertContains(response, self.sample_bug.status)

    def test_register_duplicate_bug(self):
        """
        This test checks that bug_description to ensure that duplicate bug cannot be registered.
        """
        post_data = self.valid_bug_data.copy()
        post_data ['bug_description'] ='Bug with duplicate description'
        url = reverse('bug:register_bug')
        response = self.client.post(url, post_data, follow=True)    

        self.assertEqual(response.status_code, 200)  
        bug_count = Bug.objects.filter(bug_description='Bug with duplicate description').count()
        self.assertEqual(bug_count, 1)     


    def test_future_date_rejection(self):
        """
        This test ensures that bug with future dates will be rejected.
        """
        future_date = timezone.now().date() + datetime.timedelta(days=7)
        post_data = self.valid_bug_data.copy()
        post_data['report_date'] = future_date
        
        response = self.client.post(reverse('bug:register_bug'), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bug.objects.count(), 0)

    def test_past_question(self):
        """
        Bugs with a report_date in the past are displayed on the index page.
        """
        past_date = timezone.now().date() - datetime.timedelta(days=7)
        post_data = self.valid_bug_data.copy()
        post_data['report_date'] = past_date
        
        response = self.client.post(reverse('bug:register_bug'), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bug.objects.count(), 0)