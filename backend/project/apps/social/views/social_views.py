from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.core.utils import alert_levels
from apps.social.models import SocialAction


class ListSocialActionsView(View):
    def get(self, request):
        template_name = "social/list_social_actions.html"
        actions = SocialAction.objects.all()
        f = actions.first()
        context = {"actions": actions}
        return render(request, template_name, context)

    def post(self, request):
        template_name = "social/list_social_actions.html"
        actions = SocialAction.objects.all()
        context = {"actions": actions}
        data = request.POST

        if not self.valid_data(dt=data):
            context["title"] = data.get("title")
            context["desctiption"] = data.get("desctiption")
            context["multiplier"] = data.get("multiplier")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        if self.registered_social_action(data=data):
            context["name"] = data.get("name")

            messages.add_message(
                request,
                messages.WARNING,
                "Ação social já registrada",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_social_action(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Ação social adicionada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("social_actions")

    def register_social_action(self, data):
        title = data.get("title")
        desctiption = data.get("desctiption")
        multiplier = data.get("multiplier")

        SocialAction.objects.create(
            title=title,
            desctiption=desctiption,
            multiplier=multiplier,
        )

    def registered_social_action(self, data):
        actions_query = SocialAction.objects.filter(title=data.get("title"))
        if actions_query.exists():
            return True
        return False

    def valid_data(self, dt):
        if (
            (dt.get("title") is None or dt.get("title") == "")
            or (dt.get("desctiption") is None or dt.get("desctiption") == "")
            or (dt.get("multiplier") is None or dt.get("multiplier") == "")
        ):
            return False
        return True
