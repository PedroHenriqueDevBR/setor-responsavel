from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.core.utils import alert_levels
from apps.users.models import Employee, User, Sector, Subsidiary


class ListUserView(View):
    def get(self, request):
        template_name = "users/users_list.html"
        context = {"employeers": Employee.objects.all()}
        context["subsidiaries"] = Subsidiary.objects.all()
        return render(request, template_name, context)

    def post(self, request):
        template_name = "users/users_list.html"
        context = {"employeers": Employee.objects.all()}
        context["subsidiaries"] = Subsidiary.objects.all()
        data = request.POST

        if not self.is_valid_data(data=data):
            context["first_name"] = data.get("first_name")
            context["last_name"] = data.get("last_name")
            context["identifier"] = data.get("identifier")
            context["contact"] = data.get("contact")
            context["mail"] = data.get("mail")
            context["sector"] = data.get("sector")
            context["password"] = data.get("password")
            context["repeat_password"] = data.get("repeat_password")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_employee(data)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Colaborador adicionado",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("users")

    def register_employee(self, data):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        identifier = data.get("identifier")
        contact = data.get("contact")
        mail = data.get("mail")
        sector_id = data.get("sector")
        password = data.get("password")

        user = User.objects.create_user(
            username=identifier,
            email=mail,
            password=password,
        )
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        sector = self.get_sector(sector_id)

        Employee.objects.create(
            contact=contact,
            identifier=identifier,
            sector=sector,
            user=user,
        )

    def get_sector(self, pk):
        sector_query = Sector.objects.filter(pk=pk)
        if not sector_query.exists():
            return
        return sector_query.first()

    def is_valid_data(self, data):
        if (
            (data.get("first_name") is None or data.get("first_name") == "")
            or (data.get("last_name") is None or data.get("last_name") == "")
            or (data.get("identifier") is None or data.get("identifier") == "")
            or (data.get("contact") is None or data.get("contact") == "")
            or (data.get("mail") is None or data.get("mail") == "")
            or (data.get("sector") is None or data.get("sector") == "")
            or (data.get("password") is None or data.get("password") == "")
            or (
                data.get("repeat_password") is None or data.get("repeat_password") == ""
            )
        ):
            return False

        if data.get("password") != data.get("repeat_password"):
            return False

        return True


class EditUserView(View):
    def get(self, request, pk):
        employee_query = Employee.objects.filter(pk=pk)
        if not employee_query.exists():
            return redirect("users")

        template_name = "users/user_edit.html"
        context = {"employee": employee_query.first()}
        context["subsidiaries"] = Subsidiary.objects.all()
        return render(request, template_name, context)

    def post(self, request, pk):
        employee_query = Employee.objects.filter(pk=pk)
        if not employee_query.exists():
            return redirect("users")

        employee = employee_query.first()
        template_name = "users/user_edit.html"
        context = {
            "employee": employee,
            "subsidiaries": Subsidiary.objects.all(),
        }

        data = request.POST
        if not self.is_valid_data(data=data):
            context["first_name"] = data.get("first_name")
            context["last_name"] = data.get("last_name")
            context["contact"] = data.get("contact")
            context["mail"] = data.get("mail")
            context["sector"] = data.get("sector")

            messages.add_message(
                request,
                messages.WARNING,
                "Preencha todos os campos",
                extra_tags=alert_levels.WARNING,
            )

            return render(request, template_name, context)

        self.register_employee(data, employee)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Dados atualizados",
            extra_tags=alert_levels.SUCCESS,
        )
        return redirect("users")

    def register_employee(self, data, employee):
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        contact = data.get("contact")
        mail = data.get("mail")
        sector_id = data.get("sector")

        user = employee.user
        user.email = mail
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        sector = self.get_sector(sector_id)
        employee.contact = contact
        employee.sector = sector
        employee.save()

    def get_sector(self, pk):
        sector_query = Sector.objects.filter(pk=pk)
        if not sector_query.exists():
            return
        return sector_query.first()

    def is_valid_data(self, data):
        if (
            (data.get("first_name") is None or data.get("first_name") == "")
            or (data.get("last_name") is None or data.get("last_name") == "")
            or (data.get("contact") is None or data.get("contact") == "")
            or (data.get("mail") is None or data.get("mail") == "")
            or (data.get("sector") is None or data.get("sector") == "")
        ):
            return False
        return True
