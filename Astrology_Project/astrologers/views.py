from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import AstrologerProfileSerializer
from .models import AstrologerProfile

# Create your views here.

class IsAstrologer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ASTROLOGER'

class AstrologerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = AstrologerProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAstrologer]

    def get_queryset(self):
        return AstrologerProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)