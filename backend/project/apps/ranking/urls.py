from django.urls import path
from apps.ranking.views import score_views, award_views, ranking_views

urlpatterns = [
    # Ranking
    path(
        "",
        ranking_views.CurrentRanking.as_view(),
        name="current_ranking",
    ),
    path(
        "all",
        ranking_views.ListAllRankingsView.as_view(),
        name="rankings",
    ),
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
    # Award
    path(
        "award",
        award_views.ListAwardsView.as_view(),
        name="awards",
    ),
    # Actions
    path(
        "<int:ranking_pk>/sectors/<int:sector_pk>/increase",
        ranking_views.IncreaseActionView.as_view(),
        name="increase_action",
    ),
    path(
        "<int:ranking_pk>/sectors/<int:sector_pk>/decrease",
        ranking_views.DecreaseActionView.as_view(),
        name="decrease_action",
    ),
]
