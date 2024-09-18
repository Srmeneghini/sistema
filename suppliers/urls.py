from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supliers/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supliers/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supliers/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supliers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
]
