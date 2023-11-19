from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.core.utils import alert_levels
from apps.ranking.models import Scores


class ListIncreaseScoreView(View):
    def get(self, request):
        template_name = "ranking/score/list_scores.html"
        context = {
            "title": "Pontuações",
            "scores": Scores.objects.filter(identifier=Scores.INCREASE),
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = "ranking/score/list_scores.html"
        context = {
            "title": "Pontuações",
            "scores": Scores.objects.filter(identifier=Scores.INCREASE),
        }
        data = request.POST

        if not self.valid_data(data=data):
            context["name"] = data.get("name")
            context["quantity"] = data.get("quantity")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        if self.registered_score(data=data):
            context["name"] = data.get("name")

            messages.add_message(
                request,
                messages.WARNING,
                "Pontuação já registrada",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_score(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Pontuação adicionada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("increases")

    def register_score(self, data):
        name = data.get("name")
        quantity = data.get("quantity")
        Scores.objects.create(
            name=name,
            quantity=quantity,
            identifier=Scores.INCREASE,
        )

    def registered_score(self, data):
        scores_query = Scores.objects.filter(
            name=data.get("name"),
            identifier=Scores.INCREASE,
        )
        if scores_query.exists():
            return True
        return False

    def valid_data(self, data):
        if (data.get("name") is None or data.get("name") == "") or (
            data.get("quantity") is None or data.get("quantity") == ""
        ):
            return False
        return True


class ListDecreaseScoreView(View):
    def get(self, request):
        template_name = "ranking/score/list_scores.html"
        context = {
            "title": "Penalidades",
            "scores": Scores.objects.filter(identifier=Scores.DECREASE),
        }
        return render(request, template_name, context)

    def post(self, request):
        template_name = "ranking/score/list_scores.html"
        context = {
            "title": "Penalidades",
            "scores": Scores.objects.filter(identifier=Scores.DECREASE),
        }
        data = request.POST

        if not self.valid_data(data=data):
            context["name"] = data.get("name")
            context["quantity"] = data.get("quantity")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        if self.registered_score(data=data):
            context["name"] = data.get("name")

            messages.add_message(
                request,
                messages.WARNING,
                "Penalidade já registrada",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_score(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Penalidade adicionada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("decreases")

    def register_score(self, data):
        name = data.get("name")
        quantity = data.get("quantity")
        Scores.objects.create(
            name=name,
            quantity=quantity,
            identifier=Scores.DECREASE,
        )

    def registered_score(self, data):
        scores_query = Scores.objects.filter(
            name=data.get("name"),
            identifier=Scores.DECREASE,
        )
        if scores_query.exists():
            return True
        return False

    def valid_data(self, data):
        if (data.get("name") is None or data.get("name") == "") or (
            data.get("quantity") is None or data.get("quantity") == ""
        ):
            return False
        return True
