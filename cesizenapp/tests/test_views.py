import pytest

@pytest.mark.django_db
def test_home_view(client):
    response = client.get('/')
    assert response.status_code == 200