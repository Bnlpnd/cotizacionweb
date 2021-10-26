from django.urls import path
from .views import (
    ModeloCreateView, 
    ModeloDetailView, 
    ModeloDeleteView,
    ModeloListView,
    ModeloUpdateView,
    
)

app_name = 'modelo' 
urlpatterns = [
    path('', ModeloListView.as_view(), name='modelo_list'),
    path('create/', ModeloCreateView.as_view(), name='modelo_create'),
    path('<int:id>/', ModeloDetailView.as_view(), name='modelo_detail'),
    path('<int:id>/update/', ModeloUpdateView.as_view(), name='modelo_update'),
    path('<int:id>/delete/', ModeloDeleteView.as_view(), name='modelo_delete'),
]
