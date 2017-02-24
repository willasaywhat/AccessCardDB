from django.shortcuts import render
from django.http import JsonResponse
from cards.models import Card
from logs.models import Log
import datetime
# Create your views here.


def scan_card(request, scanned_card):
    now = datetime.datetime.now()
    c = Card.objects.filter(card=scanned_card).first()
    if c is not None:
        Log.objects.create(card_scanned=scanned_card, member_name=c.member.name, status_at_scan=c.member.status)
        res = {'now': now, 'status': c.member.status}
    else:
        Log.objects.create(card_scanned=scanned_card, status_at_scan=0)
        res = {'now': now, 'status': 0}
    return JsonResponse(res)