from boutique.models import LigneVente
from boutique.models import Vente
from boutique.models import Produit
from boutique.models import Client
from rest_framework import serializers
    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','nom','prenom','username','email']

class ClientVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','nom','prenom']

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        return instance

class LigneVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneVente
        fields = ('quantite', 'prixHT', 'produit')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["produit"] = ProduitSerializer(instance.produit).data
        return data
    
    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        return instance
    
class VenteSerializer(serializers.ModelSerializer):
    lignesVente = LigneVenteSerializer(many=True)

    class Meta:
        model = Vente
        fields = ('id', 'client', 'dateVente', 'numeroVente', 'prixProduitsHT', 'prixProduitsTTC', 'lignesVente')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["client"] = ClientVenteSerializer(instance.client).data
        return data
    
    def create(self, validated_data):
        lignes_vente_data = validated_data.pop('lignesVente')
        vente_instance = Vente.objects.create(**validated_data)
        
        for ligne_vente_data in lignes_vente_data:
            LigneVente.objects.create(
                vente=vente_instance,
                **ligne_vente_data
            )

        return vente_instance
    
    def update(self, vente_instance, validated_data):
        lignes_vente_data = validated_data.pop('lignesVente')
        
        # delete existing lignesVente before adding new set
        lignesVente = vente_instance.lignesVente.all()
        for ligne_vente_previous in lignesVente:
            ligne_vente_previous.delete()

        for ligne_vente_data in lignes_vente_data:
            LigneVente.objects.create(
                vente=vente_instance,
                **ligne_vente_data
            )

        super().update(vente_instance, validated_data)

        return vente_instance