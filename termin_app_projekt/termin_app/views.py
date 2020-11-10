from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

"""Login view for LDAP sign in"""
def loginView(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

"""Home view to see all allowed appointments in a calendar"""
def homeView(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
