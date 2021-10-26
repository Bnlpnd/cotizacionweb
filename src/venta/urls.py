from django.urls import path
from django.urls.conf import include
from .views import (
    VentaCreateView, 
    VentaDetailView, 
    VentaDeleteView,
    VentaListView,
    VentaUpdateView,
    
)

app_name = 'venta'
urlpatterns = [
    path('', VentaListView.as_view(), name='venta_list'),
    path('create/', VentaCreateView.as_view(), name='venta_create'),
    path('<int:id>/', VentaDetailView.as_view(), name='venta_detail'),
    path('<int:id>/update/', VentaUpdateView.as_view(), name='venta_update'),
    path('<int:id>/delete/', VentaDeleteView.as_view(), name='venta_delete'),
    
]
