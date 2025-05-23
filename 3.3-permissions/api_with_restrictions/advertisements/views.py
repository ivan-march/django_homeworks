from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .models import Advertisement, FavoriteAdvertisement
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    permission_classes = []

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'favorite':
            return [IsAuthenticated()]
        return super().get_permissions()

    
    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        """Добавляет объявление в избранное"""

        advertisement = self.get_object()

        if advertisement.creator == request.user:
            return Response(
                {'error': 'Нельзя добавить собственно объявление в избранное.'}, status=status.HTTP_400_BAD_REQUEST
            )
        
        _, created = FavoriteAdvertisement.objects.get_or_create(
            creator=request.user,
            advertisement=advertisement
        )

        if not created:
            return Response(
                {'message': 'Объявление уже в избранном'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response({'message': 'Объявление добавлено в избранное'}, status=status.HTTP_201_CREATED)


    def get_queryset(self):
        user = self.request.user

        if self.action == 'list' and 'favorites' in self.request.query_params:
            if user.is_authenticated:
                return Advertisement.objects.filter(favorites__creator=user).filter(
                    models.Q(creator=user) | ~models.Q(status='DRAFT')
                )
            else:
                return Advertisement.objects.none()

        queryset = Advertisement.objects.all()

        if user.is_superuser:
            return queryset
        
        if user.is_authenticated:
            return queryset.filter(
                models.Q(creator=user) | ~models.Q(status='DRAFT')
            )

        return queryset.exclude(status='DRAFT')
