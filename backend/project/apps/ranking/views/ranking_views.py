from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.core.utils import alert_levels
from apps.ranking.models import Ranking, Award, Action, Scores
from apps.social.models import SocialAction
from apps.users.models import Subsidiary, Sector


class CurrentRanking(View):
    def get(self, request):
        template_name = "ranking/ranking/current_ranking.html"
        current_rankings = Ranking.objects.filter(done=False)
        if not current_rankings.exists():
            return redirect("rankings")

        ranking = current_rankings.first()
        actions = []
        subsidiaries = []
        if ranking is not None:
            subsidiaries = Subsidiary.objects.all()
            actions = ranking.ranking_actions.all()
        context = {
            "ranking": ranking,
            "subsidiaries": subsidiaries,
            "actions": actions,
        }
        return render(request, template_name, context)


class ListAllRankingsView(View):
    def get(self, request):
        template_name = "ranking/ranking/list_rankings.html"
        rankings = Ranking.objects.all()
        social_actions = SocialAction.objects.all()
        awards = Award.objects.all()
        context = {
            "rankings": rankings,
            "social_actions": social_actions,
            "awards": awards,
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = "ranking/ranking/list_rankings.html"
        rankings = Ranking.objects.all()
        social_actions = SocialAction.objects.all()
        awards = Award.objects.all()
        context = {
            "rankings": rankings,
            "social_actions": social_actions,
            "awards": awards,
        }
        data = request.POST

        if not self.valid_data(dt=data):
            context["title"] = data.get("title")
            context["description"] = data.get("description")
            context["initial_date"] = data.get("initial_date")
            context["final_date"] = data.get("final_date")
            context["social"] = data.get("social")
            context["award"] = data.get("award")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_ranking(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Premiação adicionada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("rankings")

    def get_social_action(self, id):
        social_query = SocialAction.objects.filter(pk=id)
        if social_query.exists():
            return social_query.first()
        return

    def get_award(self, id):
        award_query = Award.objects.filter(pk=id)
        if award_query.exists():
            return award_query.first()
        return

    def register_ranking(self, data):
        title = data.get("title")
        description = data.get("description")
        initial_date = data.get("initial_date")
        final_date = data.get("final_date")
        social = self.get_social_action(id=data.get("social"))
        award = self.get_award(id=data.get("award"))
        self.disable_another_rankings()

        Ranking.objects.create(
            title=title,
            description=description,
            initial_date=initial_date,
            final_date=final_date,
            social=social,
            award=award,
        )

    def disable_another_rankings(self):
        rankings = Ranking.objects.filter(done=False)
        for ranking in rankings:
            ranking.done = True
            ranking.save()

    def valid_data(self, dt):
        if (
            (dt.get("title") is None or dt.get("title") == "")
            or (dt.get("description") is None or dt.get("description") == "")
            or (dt.get("initial_date") is None or dt.get("initial_date") == "")
            or (dt.get("final_date") is None or dt.get("final_date") == "")
            or (dt.get("social") is None or dt.get("social") == "")
            or (dt.get("award") is None or dt.get("award") == "")
        ):
            return False
        return True


class IncreaseActionView(View):
    def get(self, request, ranking_pk, sector_pk):
        template_name = "ranking/score/action_sector.html"
        rankings_query = Ranking.objects.filter(pk=ranking_pk)
        sectors_query = Sector.objects.filter(pk=sector_pk)
        if not rankings_query.exists() or not sectors_query.exists():
            return redirect("rankings")

        ranking = rankings_query.first()
        scores = Scores.objects.filter(identifier=Scores.INCREASE)
        context = {
            "ranking": ranking,
            "scores": scores,
            "sector": sectors_query.first(),
            "title": "Adicionar pontos",
        }
        return render(request, template_name, context)

    def post(self, request, ranking_pk, sector_pk):
        template_name = "ranking/score/action_sector.html"
        rankings_query = Ranking.objects.filter(pk=ranking_pk)
        sectors_query = Sector.objects.filter(pk=sector_pk)
        if not rankings_query.exists() or not sectors_query.exists():
            return redirect("rankings")

        ranking = rankings_query.first()
        sector = sectors_query.first()
        scores = Scores.objects.filter(identifier=Scores.INCREASE)
        context = {
            "ranking": ranking,
            "scores": scores,
            "sector": sector,
            "title": "Adicionar pontos",
        }
        data = request.POST

        if not self.valid_data(dt=data):
            messages.add_message(
                request,
                messages.WARNING,
                "Formulário inválido",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_action(ranking=ranking, sector=sector, data=data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Ação registrada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("current_ranking")

    def get_score(self, pk):
        scores_query = Scores.objects.filter(pk=pk)
        if scores_query.exists():
            return scores_query.first()
        return

    def register_action(self, ranking, sector, data):
        score = self.get_score(pk=data.get("score"))
        Action.objects.create(ranking=ranking, sector=sector, score=score)

    def valid_data(self, dt):
        if dt.get("score") is None or dt.get("score") == "":
            return False
        return True


class DecreaseActionView(View):
    def get(self, request, ranking_pk, sector_pk):
        template_name = "ranking/score/action_sector.html"
        rankings_query = Ranking.objects.filter(pk=ranking_pk)
        sectors_query = Sector.objects.filter(pk=sector_pk)
        if not rankings_query.exists() or not sectors_query.exists():
            return redirect("rankings")

        ranking = rankings_query.first()
        scores = Scores.objects.filter(identifier=Scores.DECREASE)
        context = {
            "ranking": ranking,
            "scores": scores,
            "sector": sectors_query.first(),
            "title": "Remover pontos",
        }
        return render(request, template_name, context)

    def post(self, request, ranking_pk, sector_pk):
        template_name = "ranking/score/action_sector.html"
        rankings_query = Ranking.objects.filter(pk=ranking_pk)
        sectors_query = Sector.objects.filter(pk=sector_pk)
        if not rankings_query.exists() or not sectors_query.exists():
            return redirect("rankings")

        ranking = rankings_query.first()
        sector = sectors_query.first()
        scores = Scores.objects.filter(identifier=Scores.DECREASE)
        context = {
            "ranking": ranking,
            "scores": scores,
            "sector": sector,
            "title": "Remover pontos",
        }
        data = request.POST

        if not self.valid_data(dt=data):
            messages.add_message(
                request,
                messages.WARNING,
                "Formulário inválido",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_action(ranking=ranking, sector=sector, data=data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Ação registrada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("current_ranking")

    def get_score(self, pk):
        scores_query = Scores.objects.filter(pk=pk)
        if scores_query.exists():
            return scores_query.first()
        return

    def register_action(self, ranking, sector, data):
        score = self.get_score(pk=data.get("score"))
        Action.objects.create(ranking=ranking, sector=sector, score=score)

    def valid_data(self, dt):
        if dt.get("score") is None or dt.get("score") == "":
            return False
        return True
