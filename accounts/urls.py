from django.urls import path
from django.contrib.auth.views import LoginView
from accounts.views import (RegisterView,home_view,logout_view)



urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name='login'),#login view avalibale from django 1.11
    path('accounts/profile/',home_view),
    path('logout/',logout_view,name='logout')
]
