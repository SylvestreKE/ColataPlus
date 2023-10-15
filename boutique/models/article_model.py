from django.db import models

from compte.models import Vendeur

TYPE_ARTICLE =(
    ()
)
class Article(models.Model):
    labelle = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='Article')
    photo1 = models.ImageField(blank=True,upload_to='Article')
    photo2 = models.ImageField(blank=True,upload_to='Article')
    photo3 = models.ImageField(blank=True,upload_to='Article')
    photo4 = models.ImageField(blank=True,upload_to='Article')
    prix_base = models.PositiveIntegerField()
    quantiter = models.PositiveIntegerField(default=1)
    vendeur = models.ForeignKey(Vendeur,on_delete=models.CASCADE)
    type_article = models.CharField(choices=TYPE_ARTICLE)
    is_disponible = models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return self.labelle
