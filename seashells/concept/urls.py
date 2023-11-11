from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comparing/', views.compare_countries_view, name='comparing'),
]
