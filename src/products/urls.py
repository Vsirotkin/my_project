from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_initial_data, name='render_view'),
    # path('product/', views.product_detail_view, name='product_detail_view'),
]
