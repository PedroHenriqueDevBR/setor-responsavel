from django.urls import path
from apps.users.views import users_views

urlpatterns = [
    path("login", users_views.Login.as_view(), name="login"),
    path("logout", users_views.Logout.as_view(), name="logout"),
]
