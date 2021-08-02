from django.contrib import admin
from .views import *  # steric ka mtlb hai sb views.py import hojayen
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', (get_products)),  # http://localhost:8000/api
    # http://localhost:8000/api/productdetail/1
    path('productdetail/<int:id>/', (product_detail)),
    path('addreview/<int:id>/', (add_review)),
    path('dosignup/', (signup)),
    # .................
    # cart urls
    path('order/', getOrders, name='orders'),
    path('order/add/', addOrderItems, name='orders-add'),
    path('order/myorders/', getMyOrders, name='myorders'),
    path('orders/<int:pk>/', getOrderById, name=''),


    path('order/<str:pk>/deliver/', updateOrderToDelivered, name='order-delivered'),

    path('order/<str:pk>/', getOrderById, name='user-order'),
    path('order/<str:pk>/pay/', updateOrderToPaid, name='pay'),
    path('productcategory/<str:category>/', productsCategory)



]
