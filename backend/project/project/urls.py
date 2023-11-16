from django.contrib import admin
from django.urls import path, include
from apps.users import urls as users_urls
from apps.core.views import home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_views.home, name="index"),
    path("users/", include(users_urls)),
]
