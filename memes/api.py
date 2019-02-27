from rest_framework.viewsets import ModelViewSet

from .models import Meme
from .serializers import MemeSerializer


class MemeViewSet(ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
