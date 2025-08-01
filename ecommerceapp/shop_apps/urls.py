from django.urls import path
from . import views


urlpatterns = [
    path("products", views.products, name="products"),
    path("product_detail/<slug:slug>", views.product_detail, name="product-detail"),
    path("add_item/", views.add_item, name="add_item"),
    path("products_in_cart/", views.products_in_cart, name="products_in_cart"),
    path('cart_status/', views.get_cart_status, name="cart_status"),
    path('get_cart/', views.get_cart, name="get_cart"),
    path("update_quantity/", views.update_quantity, name="update-quantity")
]