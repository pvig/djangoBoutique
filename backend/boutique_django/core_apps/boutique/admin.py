from django.contrib import admin
from django import forms

from .models import Client
from .models import Produit
from .models import Vente
from .models import LigneVente

admin.site.empty_value_display = "(Pas de valeur)"


class LigneVenteForm(forms.ModelForm):
    class Meta:
        model = LigneVente
        fields = ["produit", "quantite", "prixHT"]

    def __init__(self, *args, **kwargs):
        super(LigneVenteForm, self).__init__(*args, **kwargs)
        self.fields["produit"].widget = forms.Select(
            choices=self.fields["produit"].choices
        )
        if self.instance and self.instance.pk:
            self.fields["produit"].disabled = True


class lignesVenteInline(admin.TabularInline):
    model = LigneVente
    form = LigneVenteForm
    verbose_name = "Produit commandé"
    verbose_name_plural = "Produits commandés"
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        for form in formset.form.base_fields.values():
            form.disabled = False
        return formset


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "email",
    )
    exclude = ["password"]


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "prixHT",
        "poids",
        "reference",
    )


class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = [
            "client",
            "dateVente",
            "prixProduitsHT",
            "prixProduitsTTC",
        ]

    def __init__(self, *args, **kwargs):
        super(VenteForm, self).__init__(*args, **kwargs)
        self.fields["client"].widget = forms.Select(
            choices=self.fields["client"].choices
        )
        if self.instance and self.instance.pk:
            self.fields["client"].disabled = True


@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    form = VenteForm
    list_display = (
        "client",
        "dateVente",
        "prixProduitsHT",
        "prixProduitsTTC",
        "nb_produits",
    )
    inlines = [lignesVenteInline]

    def nb_produits(self, obj):
        return obj.lignesVente.count()
