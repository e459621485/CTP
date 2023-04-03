from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .backend.main import run
import threading


def debug(request):
    res = {'code': 0, 'msg': 'success'}
    t = threading.Thread(target=run)
    t.start()
    return JsonResponse(res)
