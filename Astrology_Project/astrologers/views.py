from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import AstrologerProfileSerializer
from .models import AstrologerProfile
from rest_framework import generics

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


class PublicAstologerListView(generics.ListAPIView):
    serializer_class = AstrologerProfileSerializer

    def get_queryset(self):
        queryset = AstrologerProfile.objects.filter(is_approved=True)
        language = self.request.query_params.get('language')
        expertise = self.request.query_params.get('expertise')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if language:
            queryset = queryset.filter(language_spoken_contains = [language])
        if expertise:
            queryset = queryset.filter(expertise__contains = [expertise])
        if min_price:
            queryset = queryset.filter(price_per_minute__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_minute__lte=max_price)
        return queryset