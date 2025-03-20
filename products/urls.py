from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('brand/<str:brand_name>/', views.brand_products, name='brand_products'),
    path('categorie/<slug:slug>/', views.category_products, name='category_products'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)