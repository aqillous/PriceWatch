from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from .models import TrackedProduct, PriceHistory
from .serializers import TrackedProductSerializer, PriceHistorySerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class TrackedProductViewSet(viewsets.ModelViewSet):
    serializer_class = TrackedProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            TrackedProduct.objects
            .filter(user=self.request.user)
            .select_related("product")
            )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"])
    def history(self, request, pk=None):
        tracked_product = self.get_object()
        history = PriceHistory.objects.filter(product=tracked_product.product).order_by("-recorded_at")
        serializer = PriceHistorySerializer(history, many=True)
        return Response(serializer.data)



