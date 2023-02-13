from django.urls import path, include, re_path
from .views import *

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [
#     path('', home, name='users-home'),
    path('', include('social_django.urls', namespace='social')),
    
    path('register/', RegisterView.as_view(), name='users-register'),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

#     path('login/', loginView, name='login'),


    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

     # path('oauth/', include('social_django.urls', namespace='social')),
     path('profile-view/<int:pk>',EditView.as_view(), name='profileDetail'),

# email verify url
     # path('../varify-email/<token>', verify, name='verify'),


     # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
     # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
     # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
     # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),









]
