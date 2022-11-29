from django.urls import path,include
from .views import CategoriaView,CategoriaViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)


urlpatterns = [
    path('',CategoriaView.as_view()),
    path('rest', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
