from django.urls import path
from apps.users.views import auth, user_views, subsidiary_views

urlpatterns = [
    # Users
    path("", user_views.ListUserView.as_view(), name="users"),
    path("<int:pk>/edit", user_views.EditUserView.as_view(), name="user_edit"),
    # Auth
    path("login", auth.Login.as_view(), name="login"),
    path("logout", auth.Logout.as_view(), name="logout"),
    # Users
    path(
        "subsidiary",
        subsidiary_views.ListSubsidiaryView.as_view(),
        name="subsidiaries",
    ),
    path(
        "subsidiary/<int:pk>/sectors",
        subsidiary_views.ListSectorView.as_view(),
        name="sectors",
    ),
]
