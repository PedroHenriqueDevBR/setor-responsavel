from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from apps.core.utils import alert_levels
from apps.users.models import Subsidiary, Sector


class ListSubsidiaryView(View):
    def get(self, request):
        template_name = "subsidiary/subsidiary_list.html"
        context = {"subsidiaries": Subsidiary.objects.all()}
        return render(request, template_name, context)

    def post(self, request):
        template_name = "subsidiary/subsidiary_list.html"
        context = {"subsidiaries": Subsidiary.objects.all()}
        data = request.POST

        if not self.valid_data(data=data):
            context["name"] = data.get("name")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        if self.registered_subsidiary(data=data):
            context["name"] = data.get("name")

            messages.add_message(
                request,
                messages.WARNING,
                "Unidade já registrada",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_subsidiary(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Unidade adicionada",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("subsidiaries")

    def register_subsidiary(self, data):
        name = data.get("name")
        Subsidiary.objects.create(name=name)

    def registered_subsidiary(self, data):
        subsidiary_query = Subsidiary.objects.filter(name=data.get("name"))
        if subsidiary_query.exists():
            return True
        return False

    def valid_data(self, data):
        if data.get("name") is None or data.get("name") == "":
            return False
        return True


class ListSectorView(View):
    def get(self, request, pk):
        template_name = "sector/sector_list.html"
        subsidiary_query = Subsidiary.objects.filter(pk=pk)
        if not subsidiary_query.exists():
            return redirect("subsidiaries")

        subsidiary = subsidiary_query.first()
        context = {
            "sectors": subsidiary.sectors.all(),
            "subsidiary": subsidiary,
        }
        return render(request, template_name, context)

    def post(self, request, pk):
        template_name = "sector/sector_list.html"
        subsidiary_query = Subsidiary.objects.filter(pk=pk)
        if not subsidiary_query.exists():
            return redirect("subsidiaries")

        subsidiary = subsidiary_query.first()
        context = {
            "sectors": subsidiary.sectors.all(),
            "subsidiary": subsidiary,
        }
        data = request.POST

        if not self.valid_data(data=data):
            context["name"] = data.get("name")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_sector(data, subsidiary)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Setor adicionado",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect(f"/users/subsidiary/{pk}/sectors")

    def register_sector(self, data, subsidiary):
        name = data.get("name")
        Sector.objects.create(name=name, subsidiary=subsidiary)

    def valid_data(self, data):
        if data.get("name") is None or data.get("name") == "":
            return False
        return True
