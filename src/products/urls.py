from django.urls import path

from . import views

urlpatterns = [
    path('<int:my_id>', views.dynamic_lookup_view, name='look_up'),
    # path('product/', views.product_detail_view, name='product_detail_view'),
]
