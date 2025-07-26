from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AstrologerProfileViewSet

router = DefaultRouter()
router.register(r'profile', AstrologerProfileViewSet, basename='astrolger-profile')


urlpatterns = [
    path('', include(router.urls))
]