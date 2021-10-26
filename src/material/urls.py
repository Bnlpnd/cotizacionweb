from django.urls import path
from .views import (
    MaterialCreateView, 
    MaterialDetailView, 
    MaterialDeleteView,
    MaterialListView,
    MaterialUpdateView,
    
)

app_name = 'material'
urlpatterns = [
    path('', MaterialListView.as_view(), name='material_list'),
    path('create/', MaterialCreateView.as_view(), name='material_create'),
    path('<int:id>/', MaterialDetailView.as_view(), name='material_detail'),
    path('<int:id>/update/', MaterialUpdateView.as_view(), name='material_update'),
    path('<int:id>/delete/', MaterialDeleteView.as_view(), name='material_delete'),
]
