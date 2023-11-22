from django.contrib import auth
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.core.utils import alert_levels


class Login(View):
    def get(self, request):
        template_name = "auth/login.html"
        return render(request, template_name)

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect("index")

        messages.add_message(
            request,
            messages.ERROR,
            "Invalid credencials",
            extra_tags=alert_levels.DANGER,
        )
        return redirect("login")


class Logout(View):
    def get(self, request):
        user = request.user
        if user is not None and str(user) != "AnonymousUser":
            auth.logout(request)
        return redirect("login")
