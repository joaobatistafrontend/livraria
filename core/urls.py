from django.urls import path,include
from .views import  AutorApiViewSet, CategoriaApiViewSet, EditoraApiViewSet, LivroApiViewSet
from .test.crudapiview import CategoriaView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'autores', AutorApiViewSet)
router.register(r'categorias', CategoriaApiViewSet)
router.register(r'editoras', EditoraApiViewSet)
router.register(r'livros', LivroApiViewSet)

urlpatterns = [
    path('categorias/<int:id>/',CategoriaView.as_view()),
    path('', include(router.urls),name='rest'),
    path('api-auth/', include('rest_framework.urls'))
]
