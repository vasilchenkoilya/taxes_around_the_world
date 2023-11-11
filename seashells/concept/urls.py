from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comparing/', views.compare_view, name='compare'),
    path('tax/<int:pk>/', views.TaxDetailView.as_view(), name='tax_detail'),
]
