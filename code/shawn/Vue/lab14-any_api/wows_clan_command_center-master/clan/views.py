from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from data.models import Ship, ShipInstance, Player, Clan
from data.config import api_key
import requests
import json

# For displaying the clan dashboard template
class Dashboard(TemplateView):
    template_name = "clan.html"