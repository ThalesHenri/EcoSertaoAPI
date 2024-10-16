from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ProtectedView,UserDetailView,LogoutView


urlpatterns = [
    path('api/usuario/',views.apiUsuariosLista ),
    path('api/produto/', views.apiProdutolista),
    path('api/usuario/<int:id>/', views.apiUsuariosDetalhe),
    path('api/produto/', views.apiProdutolista),
    path('api/produto/<int:id>/',views.apiProdutosDetalhe),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/',ProtectedView.as_view(),name='protected_view' ),
    path('api/protected/userdetail',UserDetailView.as_view(),name='user_detail'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/login/', views.login, name='login')  # Added login endpoint
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)