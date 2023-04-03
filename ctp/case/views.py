from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .backend.main import run
import threading
import asyncio


async def debug(request):
    res = {'code': 0, 'msg': 'success'}
    loop = asyncio.get_event_loop()
    loop.create_task(run)
    # t = threading.Thread(target=run)
    # t.start()
    return JsonResponse(res)
