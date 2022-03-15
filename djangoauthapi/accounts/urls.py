from atexit import register
from django.urls import path
from accounts.views import UserChangePasswordView, UserLoginView, UserPasswordResetView, UserRegistrationView, UserProfileView,\
    SendPasswordResetEmailView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('change_password/',UserChangePasswordView.as_view(),name='change_password'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
]
