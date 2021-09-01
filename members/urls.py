from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login_user/', views.login_user, name='login_user'),
]
