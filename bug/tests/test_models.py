from django.test import TestCase
import datetime
from ..models import Bug 
from django.utils import timezone



class BugModelTests(TestCase):

    def setUp(self):

        self.sample_bug = Bug(
            bug_description = "Sample Bug description",
            bug_type = "error",
            report_date = timezone.now().date(),
            status = "To do"
        )

    def test_bug_fields (self):
        """
        This test ensures that bug fields in the model are set and return their expected values
        """    
        self.assertEqual(str(self.sample_bug.bug_description), "Sample Bug description" )
        self.assertEqual(self.sample_bug.bug_type, "error")
        self.assertEqual(self.sample_bug.report_date, timezone.now().date())
        self.assertEqual(self.sample_bug.status, "To do")

    def test_bug_description_maxlength(self):
        """
        Test the maximun length of bug_description
        """   
        self.sample_bug.bug_description = 'A' * 1000
        with self.assertRaises(Exception):
            self.sample_bug.full_clean().save()


    def test_bug_creation(self):
        """
        Test to ensure that bug object is created correctly in the database
        """        
        self.sample_bug.save()
        self.assertEqual(Bug.objects.count(), 1)

    def test_bug_string_representation(self):
        """
        Test that the string representation of a Bug object is formatted correctly.
        """
        expected_string = f"{self.sample_bug.bug_description} ({self.sample_bug.bug_type} - Reported on {self.sample_bug.report_date.strftime('%b. %d, %Y')})"
        self.assertEqual(str(self.sample_bug), expected_string)

    def test_future_bug_rejected(self):
        """
        This test ensures that bug with future dates will be rejected.
        """     
        time = timezone.now().date() + datetime.timedelta(days=7)
        future_bug =Bug(report_date=time)
        # Verify the response status and database state
        self.assertFalse(future_bug.was_published_recently())    