from django.conf.urls import url
from grp.views import HomeView, RegisterView, ProfileView, LogoutView,\
    LoginView, EditProfileView


app_name = 'grp'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^profile/$', ProfileView.as_view(), name="profile"),
    url(r'^profile/edit/$', EditProfileView.as_view(), name="edit_profile"),


]


"""    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),"""