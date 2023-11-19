from django.urls import path
from apps.ranking.views import score_views

urlpatterns = [
    # Scores
    path(
        "increase",
        score_views.ListIncreaseScoreView.as_view(),
        name="increases",
    ),
    path(
        "decrease",
        score_views.ListDecreaseScoreView.as_view(),
        name="decreases",
    ),
]
