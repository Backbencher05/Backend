from django.db import models
from users.models import CustomUser

# Create your models here.

class AstrologerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='astrologer_profile')
    bio = models.TextField()
    experience_year = models.PositiveIntegerField()
    price_per_minute = models.DecimalField(max_digits=6, decimal_places=2)
    language_spoken = models.JSONField(default=list)
    expertise = models.JSONField(default=list)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name
