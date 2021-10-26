from django.urls import path
from .views import (
    CotizacionCreateView, 
    CotizacionDetailView, 
    CotizacionDeleteView,
    CotizacionListView,
    CotizacionUpdateView,
    
)

app_name = 'cotizacion'
urlpatterns = [
    path('', CotizacionListView.as_view(), name='cotizacion_list'),
    path('create/', CotizacionCreateView.as_view(), name='cotizacion_create'),
    path('<int:id>/', CotizacionDetailView.as_view(), name='cotizacion_detail'),
    path('<int:id>/update/', CotizacionUpdateView.as_view(), name='cotizacion_update'),
    path('<int:id>/delete/', CotizacionDeleteView.as_view(), name='cotizacion_delete'),
]
