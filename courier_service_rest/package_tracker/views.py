from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Package
from .serializers import PackageSerializer

#viewsets.ModelViewSet is a class that provides the basic CRUD operations
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(deleted_at__isnull=True)
    serializer_class = PackageSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:  # Reading is public
            return []
        return [permissions.IsAuthenticated()]  # Writing requires auth

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete() # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def deleted(self, request):
        """List of soft deleted packages"""
        packages = Package.objects.filter(deleted_at__isnull=False)
        serializer = self.get_serializer(packages, many=True)
        return Response(serializer.data)
