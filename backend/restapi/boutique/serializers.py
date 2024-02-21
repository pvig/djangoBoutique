from boutique.models import LigneVente
from boutique.models import Vente
from boutique.models import Produit
from boutique.models import Client
from rest_framework import serializers


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class LigneVenteSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    class Meta:
        model = LigneVente
        fields = ('quantite','prixHT','produit')

class VenteSerializer(serializers.ModelSerializer):
    lignesVente = LigneVenteSerializer(many=True)
    class Meta:
        model = Vente
        fields = ('id','client','dateVente','numeroVente','prixProduitsHT','prixProduitsTTC','lignesVente')

