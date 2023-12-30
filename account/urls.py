from django.urls import path
from .views import RegisterView, MyProfileView, UserUpdateView
from django.contrib.auth.views import (LoginView, 
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView)


app_name = "account"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my-profile/', MyProfileView.as_view(), name='my_profile'),
    path('profile-update/<int:id>/', UserUpdateView.as_view(), name='profile_update'),
    path('pass-change/', PasswordChangeView.as_view(), name='pass-change'),
    path('pass-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('pass-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('pass-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('pass-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('pass-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]