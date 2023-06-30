from django.urls import path
from . import views

app_name = 'phones'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
]