# ecommerce_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('store/', store_views.product_list, name='product_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)