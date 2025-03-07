from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Package(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    product_description = models.TextField(blank=True, null=True)
    tracking_number = models.CharField(max_length=20, unique=True)  
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        ordering = ['-created_at']