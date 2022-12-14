from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import  Autor, Categoria, Editora ,Livro


class AutorSeerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1