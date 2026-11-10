from rest_framework.routers import DefaultRouter
from .views import TrackedProductViewSet

router = DefaultRouter()
router.register('tracking', TrackedProductViewSet, basename='tracking')

urlpatterns = router.urls