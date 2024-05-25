from django.test import TestCase

from core_apps.boutique.models import Client


class AccountTests(TestCase):
    def setUp(self):
        Client.objects.create(username="user1", password="roar", email="", nom="")

    def test_account_can_be_created(self):
        """Account can be created"""
        user1 = Client.objects.get(username="user1")
        self.assertEqual(user1.username, "user1")
