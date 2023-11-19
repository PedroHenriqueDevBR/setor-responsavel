from django.urls import path
from apps.social.views import social_views

urlpatterns = [
    # Scores
    path(
        "",
        social_views.ListSocialActionsView.as_view(),
        name="social_actions",
    ),
]
