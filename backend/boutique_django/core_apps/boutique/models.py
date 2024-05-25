from django.db import models

# Create your models here.


class Client(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nom.capitalize()} {self.prenom.capitalize()}"


class Produit(models.Model):
    nom = models.CharField(max_length=100, blank=True, null=True)
    prixHT = models.FloatField()
    poids = models.FloatField()
    reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.reference}"


class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateVente = models.DateField()
    numeroVente = models.CharField(max_length=100, blank=False, null=False)
    prixProduitsHT = models.FloatField()
    prixProduitsTTC = models.FloatField()

    def __str__(self):
        return f"{self.client} - {self.numeroVente} - {self.dateVente}"


class LigneVente(models.Model):
    vente = models.ForeignKey(
        Vente, on_delete=models.CASCADE, related_name="lignesVente"
    )
    quantite = models.PositiveIntegerField()
    prixHT = models.FloatField()
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produit} - {self.quantite}"
