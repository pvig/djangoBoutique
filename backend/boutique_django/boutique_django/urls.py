from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# For yasg
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

from core_apps.users.views import CustomUserDetailsView

# For yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Boutique",
        default_version="v1",
        description="Boutique",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('auth/', include('auth.urls')),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("api/", include("core_apps.boutique.urls")),
    # For yasg
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("openapi/", TemplateView.as_view(template_name="swagger-ui/dist/index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
