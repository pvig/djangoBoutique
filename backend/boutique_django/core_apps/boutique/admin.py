from django.contrib import admin

from .models import Client
from .models import Produit
from .models import Vente

class ClientAdmin(admin.ModelAdmin):
    list_display=(
    'username', 'email',
)

class ProduitAdmin(admin.ModelAdmin):
    list_display=(
    'nom', 'prixHT', 'poids', 'reference',
)

class VenteAdmin(admin.ModelAdmin):
    list_display=(
    'client', 'dateVente', 'prixProduitsHT', 'prixProduitsTTC',
)


admin.site.register(Client,ClientAdmin)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Vente,VenteAdmin)