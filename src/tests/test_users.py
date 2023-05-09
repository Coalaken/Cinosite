from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve


class TestUsers(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="test_user"
        )

    def test_profile_page(self):
        url = reverse('profile', args={self.user.pk})
        function = resolve(url).func

        self.assertTrue(function)

    def test_register(self):
        url = reverse('sign_up')
        response = self.client.get()
        