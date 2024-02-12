from django.db import models

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    dateCommande1 = models.DateField()
    dateLastCommande = models.DateField()

class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateVente = models.DateField()
    numeroVente = models.CharField(max_length=100,blank=False,null=False)
    prixProduitsHT = models.FloatField()
    prixProduitsTTC = models.FloatField()

class Produit(models.Model):
    nom = models.CharField(max_length=100,blank=True,null=True)
    prixHT = models.FloatField()
    poids = models.FloatField()
    reference = models.CharField(max_length=100,blank=True,null=True)

class LigneVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prixHT = models.FloatField()

