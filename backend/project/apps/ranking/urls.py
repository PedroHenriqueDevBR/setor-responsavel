from django.urls import path
from apps.ranking.views import score_views, award_views, ranking_views

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
    path(
        "award",
        award_views.ListAwardsView.as_view(),
        name="awards",
    ),
    path(
        "all",
        ranking_views.ListAllRankingsView.as_view(),
        name="rankings",
    ),
]
