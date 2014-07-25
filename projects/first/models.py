from django.db import models
from django.contrib.auth.models import User
class Entreprises(models.Model):
    siret = models.CharField(max_length=45)
    nom = models.CharField(max_length=45)
    slogan = models.CharField(max_length=45)
    domaine = models.CharField(max_length=45)
    pays = models.CharField(max_length=45)
    region = models.CharField(max_length=45)
    ville = models.CharField(max_length=45)
    commune = models.CharField(max_length=45)
    adresse = models.CharField(max_length=255)
    logo_entreprise = models.ImageField(null=True,upload_to="logo/entreprise")
    user = models.ForeignKey(User)
    def __unicode__(self):
        return u"%s" % self.nom
