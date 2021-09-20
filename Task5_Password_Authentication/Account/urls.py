from django.urls import path
from django.contrib.auth import views
from .views import registerView, loginView, logoutView, changePasswordView
from .views import mailSendView


urlpatterns=[
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('changepass/',changePasswordView , name='changepass'),
    path('changepass/', changePasswordView, name='changepass'),

    path('mailsend/', mailSendView, name='mailsend'),

    path('reset_password/',views.PasswordResetView.as_view(template_name='Account/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/',views.PasswordResetDoneView.as_view(template_name='Account/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='Account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/',views.PasswordResetCompleteView.as_view(template_name='Account/password_reset_complete.html'), name='password_reset_complete')


]