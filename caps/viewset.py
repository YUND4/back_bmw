from rest_framework import viewsets
from .models import Cap
from .serializers import CapSerializer

class CapViewset(viewsets.ModelViewSet):
    queryset = Cap.objects.all()
    serializer_class = CapSerializer
    permission_classes = []