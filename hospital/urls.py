from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# For Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Hospital App API (HAA)",
        default_version="v1",
        description="API documentation for HAA",
        terms_of_service="",
        contact=openapi.Contact(email="dkmezza@gmail.com"),
        license=openapi.License(name=""),
    ),
    public=True,
    # permission_classes=(IsDeveloper,),
)

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),

    # Auth
    path("api/v1/", include("hospital.accounts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/register/', include('dj_rest_auth.registration.urls')),

    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),  # api documentation
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

admin.site.site_header = "HAA Admin"
admin.site.site_title = "HAA Admin Portal"
admin.site.index_title = "Welcome to HAA Administration"
