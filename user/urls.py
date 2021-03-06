from django.contrib import admin
from django.urls import path, include
import user.views

urlpatterns = [
    path('login/', user.views.login, name="login"),
    path('signup/', user.views.signup, name="signup"),
    path('signupseller/', user.views.signupseller, name="signupseller"),
    path('signupintro/', user.views.signupintro, name="signupintro"),
]
