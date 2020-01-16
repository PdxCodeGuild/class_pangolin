import re
import requests
import json

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from data.config import api_key
from data.models import Player, Clan

from .authentication import Authentication
from .verification import Verification
from .exceptions import OpenIDVerificationFailed


class FirstStep(TemplateView):
    template_name = 'oid-login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        components = {
            'scheme': self.request.scheme,
            'host': self.request.get_host(),
            'path': reverse('wowsopenid:callback')
        }
        return_to = '{scheme}://{host}{path}'.format(**components)
        auth = Authentication(return_to=return_to)
        url = auth.authenticate('https://na.wargaming.net/id/openid/')

        context['url'] = url
        return context


class SecondStep(TemplateView):
    template_name = 'oid-callback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        regex = r'https://na.wargaming.net/id/([0-9]+)-(\w+)/'
        current = self.request.build_absolute_uri()
        verify = Verification(current)

        try:
            identities = verify.verify()
            match = re.search(regex, identities['identity'])
            context['account_id'] = match.group(1)
            context['nickname'] = match.group(2)
            context['authenticated'] = True
            self.create_user(context['nickname'], context['account_id'])


        except OpenIDVerificationFailed:
            context['authenticated'] = False
            logout(self.request)

        return context

    def create_user(self, nickname, wgid):
        realm = 'NA'
        # resolve realm
        if realm == 'NA':
            realm_url = 'com'
        elif realm == 'EU':
            realm_url = 'eu'
        elif realm == 'SEA':
            realm_url = 'asia'


        try:
            user = User.objects.get(username__exact=nickname)

        except ObjectDoesNotExist:
            password = User.objects.make_random_password(length=255)
            user = User.objects.create_user(nickname, '', password)
            user.first_name = nickname

            # try to find Player object
            p, was_created = Player.objects.get_or_create(player_wgid=wgid)
            p.player_nickname = nickname
            user.player = p

            # get clan 
            payload = {
                'application_id': api_key,
                'account_id': wgid,
            }
            response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/clans/accountinfo/", params=payload)
            page_query = json.loads(response.text)
            clan_id = page_query['data'][wgid]['clan_id']
            c, was_created = Clan.objects.get_or_create(clan_wgid=clan_id, clan_realm=realm)
            p.player_clan = c
            user.save()
            p.save()

        login(self.request, user)
        return user 


def logout_user(request):
    logout(request)
    return redirect(reverse('clan_battles:dashboard'))