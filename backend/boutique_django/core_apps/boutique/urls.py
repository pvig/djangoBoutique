from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from core_apps.boutique import views

urlpatterns = [
    path("vente/", views.VenteList.as_view()),
    path("vente/<int:pk>/", views.VenteDetail.as_view()),
    path("client/", views.ClientList.as_view()),
    path("client/<int:pk>/", views.ClientDetail.as_view()),
    path("produit/", views.ProduitList.as_view()),
    path("produit/<int:pk>/", views.ProduitDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
