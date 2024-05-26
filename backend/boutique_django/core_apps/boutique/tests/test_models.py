import pytest

from core_apps.boutique.models import Client

class TestClientInstance:
    value = 0
    
@pytest.mark.django_db
def test_create_client(normal_client):
    assert normal_client.username is not None
    assert normal_client.password is not None
    assert normal_client.email is not None
    assert normal_client.nom is not None
    assert normal_client.prenom is not None

@pytest.mark.django_db
def test_client_email_incorrect(client_factory):
    with pytest.raises(ValueError) as err:
        client_factory.create(username="test", password="test", email="", nom="test", prenom="test")
    assert str(err.value) == "You must provide a valid email address."
    
