from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaView.as_view(), name='categoria-list'),
    path('productos/', views.ProductoView.as_view(), name='producto-list'),
]
