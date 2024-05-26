from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class ClientManager(models.Manager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("You must provide a valid email address."))

    def create_client(self, nom, prenom, username, email, password, **extra_fields):
        if not nom:
            raise ValueError(_("Users must have a nom."))
        if not username:
            raise ValueError(_("Users must have a username."))
        if email:
            self.email_validator(email)
        else:
            raise ValueError(_("You must provide a valid email address."))
        
        client = self.model(
            nom=nom, prenom=prenom, username=username, email=email, password=password, **extra_fields
        )

        client.save(using=self._db)
        return client

