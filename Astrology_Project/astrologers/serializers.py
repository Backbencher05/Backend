from rest_framework import serializers
from .models import AstrologerProfile


class AstrologerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstrologerProfile
        fields = '__all__'
        read_only_fields = ['user', 'is_approved']