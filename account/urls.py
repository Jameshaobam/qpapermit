from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register',views.signup_user,name = 'signup_user'),
    path('login',views.signin_user,name = 'signin_user'),
    path('logout',views.logout_user,name = 'logout_user'),
]
