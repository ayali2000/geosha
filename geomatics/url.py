from django.urls import path
from geomatics import views

urlpatterns = [
    path('<int:pk>/',views.detail_quest,name='detail_quest'),
    path('',views.geohome,name='geohome'),
]
