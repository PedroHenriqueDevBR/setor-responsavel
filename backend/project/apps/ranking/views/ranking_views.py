from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.core.utils import alert_levels
from apps.ranking.models import Ranking


class CurrentRanking(View):
    def get(self, request):
        template_name = "ranking/ranking/current_ranking.html"
        current_rankings = Ranking.objects.filter(done=False)
        if current_rankings.exists():
            return redirect("")
        context = {"rankings": current_rankings}
        return render(request, template_name, context)


class ListAllRankingsView(View):
    def get(self, request):
        template_name = "ranking/ranking/list_rankings.html"
        rankings = Ranking.objects.all()
        context = {"awards": rankings}
        return render(request, template_name, context)

    def post(self, request):
        template_name = "ranking/award/list_awards.html"
        awards = Award.objects.all()
        context = {"awards": awards}
        data = request.POST

        if not self.valid_data(dt=data):
            context["title"] = data.get("title")
            context["description"] = data.get("description")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        if self.is_registered_award(data=data):
            context["title"] = data.get("title")
            context["description"] = data.get("description")

            messages.add_message(
                request,
                messages.WARNING,
                "Premiação já registrada",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_award(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Premiação adicionada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("awards")

    def register_award(self, data):
        title = data.get("title")
        description = data.get("description")

        Award.objects.create(
            title=title,
            description=description,
        )

    def is_registered_award(self, data):
        awards_query = Award.objects.filter(title=data.get("title"))
        if awards_query.exists():
            return True
        return False

    def valid_data(self, dt):
        if (dt.get("title") is None or dt.get("title") == "") or (
            dt.get("description") is None or dt.get("description") == ""
        ):
            return False
        return True
