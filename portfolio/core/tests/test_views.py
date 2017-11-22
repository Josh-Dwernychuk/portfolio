from django.urls import reverse


def test_home(admin_client):
    """ Test home view and ensure a proper repsonse """
    response = admin_client.get(reverse('portfolio:core'))
    assert response.status_code == 200
