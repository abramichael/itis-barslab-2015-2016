from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class homePage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login(self):
        self.assertEquals(reverse("audio:index"), '/audio/')

    def test_anon(self):
        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 200)
        response = self.client.get(reverse("audio:index"))
        self.assertEquals(response.status_code, 302)


    def test_not_anon(self):

        user = User.objects.create_user(
            username="user",
            password="user"
        )

        login_status = self.client.login(
            username='user',
            password='user'
        )

        self.assertTrue(login_status)

        response = self.client.get(reverse("login"))
        self.assertEquals(response.status_code, 302)
        response = self.client.get(reverse("audio:index"))
        self.assertEquals(response.status_code, 200)
        self.client.logout()
