from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView, TokenRefreshView
from . import views


app_name= 'accounts'
urlpatterns = [
    path("login/",  TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("signup/", views.Signup.as_view()),
    path("logout/", TokenBlacklistView.as_view()),
    path('profile/<str:username>/', views.UserProfileView.as_view()),
    path("send-email/", views.SendEmail.as_view()),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]