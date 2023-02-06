from django.urls import path

from todo.views import *

urlpatterns = [
    path('', index),
    path('login', login, name="login"),
    path('auth', auth, name="auth"),
    path('mytodo', create, name="mytodo"),
    path('logout', logout, name="logout"),
    path('register', register, name="register"),
    path('newaccount', new, name="newaccount"),
    path('task/<int:task_id>/', remove, name="remove")
]
