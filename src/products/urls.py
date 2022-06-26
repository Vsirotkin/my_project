from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_create_view, name='create_view'),
    # path('product/', views.product_detail_view, name='product_detail_view'),
]
