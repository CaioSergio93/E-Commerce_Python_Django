from django.urls import path
from . import views

urlpatterns = [
    # URL da página inicial, sem categoria
    path('', views.product_list, name='product_list'),
    
    # URL para exibir produtos por categoria
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]