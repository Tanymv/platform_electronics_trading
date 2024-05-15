from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    #  Токены авторизации для postman
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #  Работа с моделью пользователя
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]