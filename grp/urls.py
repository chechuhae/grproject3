from grp.views import HomeView, RegisterView, ProfileView, LogoutView,\
    LoginView, EditProfileView
from django.urls import path
from django.contrib.auth import views


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/edit/', EditProfileView.as_view(), name="edit_profile"),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('profile/password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('profile/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('profile/password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
