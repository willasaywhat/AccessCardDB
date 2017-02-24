from django.shortcuts import render
from django.http import JsonResponse
from cards.models import Card
import datetime
# Create your views here.


def scan_card(request, scanned_card):
    now = datetime.datetime.now()
    c = Card.objects.filter(card=scanned_card).first()
    if c is not None:
        res = {'now': now, 'status': c.member.status}
    else:
        res = {'now': now, 'status': 0}
    return JsonResponse(res)