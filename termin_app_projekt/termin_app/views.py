from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm
from django.views.decorators.http import require_http_methods


"""Login view for LDAP sign in"""
@require_http_methods(["GET", "POST"])
def loginView(request):
    if request.method == "GET":
        login_data = LoginForm()
        return render(request, "login/login.html", {'form': login_data})
    elif request.method == "POST":
        form = LoginForm(request.POST)



"""Home view to see all allowed appointments in a calendar"""
def homeView(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
