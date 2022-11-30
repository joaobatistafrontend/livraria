from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Autor, Categoria, Editora , Livro
from .serializers import AutorSeerializer, CategoriaSerializer, EditoraSerializer, LivroSerializer
import json
from rest_framework import viewsets

class AutorApiViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSeerializer

class CategoriaApiViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraApiViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroApiViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer