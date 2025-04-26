from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, RegisterView, UserMeView

router = DefaultRouter()
router.register(r'', CustomUserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', UserMeView.as_view(), name='users-me'),
    path('', include(router.urls)),
]
