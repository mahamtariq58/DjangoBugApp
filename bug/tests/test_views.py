from django.test import TestCase, Client
from django.urls import reverse
from ..models import Bug
import datetime 
from django.utils import timezone

# Test cases for views

class BugAppViewTests(TestCase):

    # setup a common data for testing
    def setUp(self):

        # instance of client
        self.client = Client()

        self.valid_bug_data = {
            'bug_description': 'Valid Bug',
            'bug_type': 'error',
            'report_date': datetime.date(2023, 10, 3),
            'status': 'To do',
        }

    def test_future_bug_rejected(self):
        
        url = reverse ('register_bug')  
        # future date calculated
        future_date = timezone.now() + datetime.timedelta(days=7)
        data = self.valid_bug_data.copy()
        data['bug_description'] = 'Future Bug'
        data['report_date'] = future_date.strftime('%Y-%m-%d')  

        # Perform a POST request to register the bug using the client
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bug.objects.count(), 0)

    def test_register_duplicate_bug(self):

        # Create a bug with a known description in the database
        existing_bug = Bug.objects.create(
            bug_description='Bug with duplicate description',
            bug_type='error',
            report_date= datetime.date(2023, 10, 3),
            status='To do',
        )

        post_data = {
            'bug_description': 'Bug with duplicate description',
            'bug_type': 'error',
            'report_date': datetime.date(2023, 10, 3),
            'status': 'To do',
        }
        
        url = reverse('register_bug')

        response = self.client.post(url, post_data, follow=True)        
        self.assertEqual(response.status_code, 200)  
        bug_count = Bug.objects.filter(bug_description='Bug with duplicate description').count()
        self.assertEqual(bug_count, 1)  


    def test_fields_bug_view(self):
        # Create a sample bug using valid_bug_data
        self.sample_bug = Bug.objects.create(
            bug_description=self.valid_bug_data['bug_description'],
            bug_type=self.valid_bug_data['bug_type'],
            report_date=self.valid_bug_data['report_date'],
            status=self.valid_bug_data['status'],
        )
        
        url = reverse('fields_bug', args=[self.sample_bug.id])
        # Perform a GET request to the fields_bug view
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.sample_bug.bug_description)
        self.assertContains(response, self.sample_bug.bug_type)
        self.assertContains(response, self.sample_bug.report_date.strftime('%b. %d, %Y').replace(' 0', ' '))
        self.assertContains(response, self.sample_bug.status)
    