from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Autor, Categoria, Editora , Livro
from .serializers import AutorSeerializer, CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer
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
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return LivroDetailSerializer
    #     if self.action == 'retrieve':
    #         return LivroDetailSerializer
    #     return LivroSerializer
    serializer_class = LivroDetailSerializer
    # serializer_class = LivroSerializer