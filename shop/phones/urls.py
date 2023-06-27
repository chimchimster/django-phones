from django.urls import path
from . import views

app_name = 'phones'

urlpatterns = [
    path('', views.product_list, name='products'),
    path('<slug:category_slug>/', views.product_list, name='list_categories'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]