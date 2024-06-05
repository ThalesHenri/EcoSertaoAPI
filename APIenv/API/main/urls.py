from django.urls import path
from . import views

urlpatterns = [
    path('api/fornecedores/',views.apiFornecedoresLista ),
    path('api/compradores/', views.apiCompradoresLista),
    path('api/fornecedores/<int:id>/', views.apiFornecedoresDetalhe),
    path('api/compradores/<int:id>/', views.apiCompradoresDetalhe)
]
