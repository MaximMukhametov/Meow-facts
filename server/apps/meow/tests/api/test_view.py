from django.urls import reverse
from rest_framework.test import APIClient


def test_get_users_view():
    """Ensure anybody can see all users."""
    url = reverse('run_task')
    response = APIClient().get(url)

    assert response.status_code == 200