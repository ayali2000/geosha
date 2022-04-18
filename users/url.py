from django.urls import path
from users import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('logout',LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('login',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('sign_up',views.sign_up,name='signup')
]
