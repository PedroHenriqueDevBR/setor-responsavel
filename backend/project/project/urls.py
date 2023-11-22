from django.contrib import admin
from django.urls import path, include
from apps.core.views import home_views
from apps.users import urls as users_urls
from apps.ranking import urls as ranking_urls
from apps.social import urls as social_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_views.home, name="index"),
    path("users/", include(users_urls)),
    path("ranking/", include(ranking_urls)),
    path("social/", include(social_urls)),
]
