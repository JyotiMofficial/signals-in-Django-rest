from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import SModel, ASModel, ThreadModel, TransactionModel
from .signals import t_handler  

def trigger_sync_signal(request):
    SModel.objects.create(name="Sync Example")
    return HttpResponse("Sync signal triggered.")

async def trigger_async_signal(request):
    await ASModel.objects.acreate(name="Async Example")
    return HttpResponse("Async signal triggered.")

def trigger_thread_signal(request):
    ThreadModel.objects.create(name="Thread Example")
    return HttpResponse("Thread signal triggered.")

def trigger_transaction_signal(request):
    obj = TransactionModel.objects.create(name="Transaction Example")
    return HttpResponse("Transaction signal triggered.")
