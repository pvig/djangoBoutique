from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

# For yasg 
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

# For yasg 
schema_view = get_schema_view(
   openapi.Info(
      title="Boutique",
      default_version='v1',
      description="Boutique",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('api/',include('core_apps.boutique.urls')),

    # For yasg 
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('openapi/', TemplateView.as_view(template_name="swagger-ui/dist/index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

