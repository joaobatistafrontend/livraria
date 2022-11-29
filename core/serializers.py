from rest_framework import routers, serializers, viewsets
from .models import Categoria

class CatedoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'descricao']