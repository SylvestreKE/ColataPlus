from django.db import models
from django.contrib.auth.models import User
from core import settings
import stripe

stripe.api_key = settings.STRIPE_API_KEY


# Create your models here.
class CustomUser(User):
    telephone = models.CharField(unique=True)
    is_client = models.BooleanField(default=True)


"""    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]"""


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
    stripe_customer_id = models.CharField(max_length=120)


class Vendeur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
