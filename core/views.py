from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Categoria
from .serializers import CatedoriaSerializer
import json
from rest_framework import viewsets


class CategoriaView(View):
    def get(self,request,id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formmated_data = json.dumps(data,ensure_ascii=False)
            return HttpResponse(formmated_data, content_type='application/jon')

    def post(self,request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {'id': nova_categoria.id, 'descricao' : nova_categoria.descricao }
        return JsonResponse(data)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CatedoriaSerializer