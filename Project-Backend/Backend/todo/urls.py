from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, register_user

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('register/', register_user),
    path('', include(router.urls))
]