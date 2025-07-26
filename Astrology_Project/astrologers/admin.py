from django.contrib import admin
from .models import AstrologerProfile

# Register your models here.

@admin.register(AstrologerProfile)
class AstrologerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience_year', 'price_per_minute', 'language_spoken', 'bio', 'is_approved', )
    list_filter = ('is_approved', 'experience_year')
    search_fields = ('user_email',)

