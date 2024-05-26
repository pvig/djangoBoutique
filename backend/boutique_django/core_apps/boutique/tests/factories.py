import factory
from core_apps.boutique.models import Client
from django.db.models.signals import post_save
from faker import Factory as FakerFactory

faker = FakerFactory.create()

@factory.django.mute_signals(post_save)
class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    nom = factory.LazyAttribute(lambda x: faker.first_name())
    prenom = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.email())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_client(*args, **kwargs)
