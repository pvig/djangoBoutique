from django.contrib import admin

from .models import Client
from .models import Produit
from .models import Vente
from .models import LigneVente

class lignesVenteInline(admin.TabularInline):
    model = LigneVente
    extra = 1
    fields = ['produit_nom', 'quantite', 'prixHT'] 
    readonly_fields = ['produit_nom'] 

class ClientAdmin(admin.ModelAdmin):
    list_display=('username', 'email',)

class ProduitAdmin(admin.ModelAdmin):
    list_display=('nom', 'prixHT', 'poids', 'reference',)

class VenteAdmin(admin.ModelAdmin):
    list_display=('client_nom', 'dateVente', 'prixProduitsHT', 'prixProduitsTTC', 'lignesVente',)
    readonly_fields = ['client_nom', 'dateVente',]
    exclude = ['client']
    inlines = [lignesVenteInline]
    def lignesVente(self, obj):
        return list(obj.lignesVente.all())
        
admin.site.register(Client,ClientAdmin)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Vente,VenteAdmin)
