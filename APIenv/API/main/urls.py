from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/fornecedores/',views.apiFornecedoresLista ),
    path('api/compradores/', views.apiCompradoresLista),
    path('api/produto/', views.apiProdutolista),
    path('api/fornecedores/<int:id>/', views.apiFornecedoresDetalhe),
    path('api/compradores/<int:id>/', views.apiCompradoresDetalhe),
    path('api/produto/', views.apiProdutolista),
    path('api/produto/<int:id>/',views.apiProdutosDetalhe),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)