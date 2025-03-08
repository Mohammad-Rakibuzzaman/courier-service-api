from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet

router = DefaultRouter()
#register the viewset with the router
router.register('packages', PackageViewSet, basename='package')
#register the viewset with the router
urlpatterns = [
    path('', include(router.urls)),
]   
# The router generates the following URL patterns:
#     GET /packages/ - List all packages