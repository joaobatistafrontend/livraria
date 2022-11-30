from django.http import HttpResponse, JsonResponse
from django.views import View
from core.models import Categoria
import json


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

    def path(self,request,id):
        json_data = json.loads(request.doby)
        qs = Categoria.objects.get(id=id)
        qs.descricao = json_data['descricao']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)

    def delete(self,request,id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {'mensagem':'item excluido com sucesso'}
        return JsonResponse(data)
