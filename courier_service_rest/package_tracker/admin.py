from django.contrib import admin
from .models import Package

@admin.register(Package)
#is a decorator that registers the PackageAdmin class with the admin site
class PackageAdmin(admin.ModelAdmin):
#PackageAdmin is a class that inherits from admin.ModelAdmin and showing to the admin site
    list_display = ('product_description', 'tracking_number', 'tracking_number', 'sender', 'receiver', 'address', 'status', 'created_at', 'updated_at', 'deleted_at')

    def is_deleted(self, obj):
        return obj.deleted_at is not None
    is_deleted.boolean = True
