from django.db import models
from boutique.models.article_model import Article
from compte.models import Client, Vendeur


# Create your models here.
class Commande(models.Model):
    numero = models.UUIDField(unique=True,auto_created=True,max_length=20)
    vendeur = models.ForeignKey(Vendeur,verbose_name="vendeur",on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, verbose_name="client", on_delete=models.CASCADE)
    article = models.ManyToManyField(Article)
    is_validate = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_created=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(f"Commande {self.numero} de {self.Client}")