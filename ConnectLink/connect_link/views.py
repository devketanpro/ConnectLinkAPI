from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Interest
from connect_link.serializers import InterestSerializer


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class InterestCreateView(generics.CreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class ReceivedInterestListView(generics.ListAPIView):
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interest.objects.filter(receiver=self.request.user, status='pending')

    
class AcceptedInterestView(generics.ListAPIView):
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interest.objects.filter(receiver=self.request.user, status='pending')
