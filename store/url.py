from django.urls import path
from store import views

urlpatterns = [
    path('',views.products,name='products'),
    path('product/<int:pk>/',views.order,name='order'),
]
