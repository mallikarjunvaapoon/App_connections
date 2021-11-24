from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, LoginView,  Verify_Email

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('email', Verify_Email.as_view(), name='email'),
    path('login', LoginView.as_view()),

]