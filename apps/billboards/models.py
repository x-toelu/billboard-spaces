from cloudinary.models import CloudinaryField

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Billboard(models.Model):
    SIZE_CHOICES = (
        ('potrait', 'Potrait'),
        ('large_format', 'Large Format'),
        ('48_sheet', '48 Sheet'),
        ('spectacular_billboard', 'Spectacular Billboard'),
        ('gantry', 'Gantry'),
        ('unipole', 'Unipole'),
    )

    owner = models.ForeignKey(
        get_user_model(),
        related_name='billboards',
        on_delete=models.CASCADE
    )
    image = CloudinaryField()
    size = models.CharField(max_length=21, choices=SIZE_CHOICES)
    location = models.CharField(max_length=255)
    target_audience = models.CharField(max_length=255)

    booked = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_verified and not self.is_verified_at:
            self.is_verified_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-is_verified_at']

    def __str__(self) -> str:
        return f"{self.owner.display_name}'s billboard at {self.location}"
