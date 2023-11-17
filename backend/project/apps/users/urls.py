from django.urls import path
from apps.users.views import auth, user_views

urlpatterns = [
    # Users
    path("", user_views.ListUserView.as_view(), name="users"),
    # Auth
    path("login", auth.Login.as_view(), name="login"),
    path("logout", auth.Logout.as_view(), name="logout"),
]
