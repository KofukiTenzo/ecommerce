from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.ApiOverview, name='overview'),
    path('', views.view_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]
