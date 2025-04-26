
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/v1/properties/', include('apps.properties.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/leases/', include('apps.leases.urls')),
    path('api/v1/payments/', include('apps.payments.urls')),
    path('api/v1/reports/', include('apps.reports.urls')),
]


schema_view = get_schema_view(
   openapi.Info(
      title="Rent API",
      default_version='v1',
      description="API documentation for rent API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
