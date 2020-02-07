from django.urls import path, re_path

from .views import (
    ProductDetailSlugView, 
    ProductListView,
    )

app_name="products"


urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
]
