from django.contrib import auth
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect


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

        else:
            return HttpResponseRedirect("Invalid username or password")
