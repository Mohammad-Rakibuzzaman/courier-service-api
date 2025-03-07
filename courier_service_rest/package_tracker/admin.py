from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('product_description', 'tracking_number', 'tracking_number', 'sender', 'receiver', 'address', 'status', 'created_at', 'updated_at', 'deleted_at')

    def is_deleted(self, obj):
        return obj.deleted_at is not None
    is_deleted.boolean = True
