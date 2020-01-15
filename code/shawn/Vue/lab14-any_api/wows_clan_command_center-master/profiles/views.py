from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class DetailPlayerView(TemplateView):
    template_name = "profile.html"

