from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .backend.main import run
import threading
import asyncio
import httpx


async def debug(request):
    res = {'code': 0, 'msg': 'success'}
    loop = asyncio.get_event_loop()
    loop.create_task(run_task_async())
    # t = threading.Thread(target=run)
    # t.start()
    return JsonResponse(res)

# 异步任务
async def run_task_async():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, run)
    # async with httpx.AsyncClient() as client:
    #     r = await client.get("https://httpbin.org/")
    #     print(r)
