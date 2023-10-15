from django.db import models
from boutique.models.article_model import Article
from compte.models import Client


# Create your models here.
class Panier(models.Model):
    user = models.OneToOneField(Client,on_delete=models.CASCADE)
    article = models.ManyToManyField(Article)
    total = models.PositiveSmallIntegerField()