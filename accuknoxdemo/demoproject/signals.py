from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from .models import SModel , ASModel ,TransactionModel , ThreadModel

import threading
from .models import ThreadModel
import asyncio


#synchronous signal handler
@receiver(post_save , sender=SModel)
def s_handler(sender , instance ,**kwargs):
    print(f"synchronously handling signals for {instance.name}")
    print(f"current Thread (synchronous ): {threading.get_ident()} ") 
    print(f"active signals : {threading.activeCount()}")



@receiver(post_save, sender=ASModel)
async def async_signal_handler(sender, instance, **kwargs):
    print(f"Starting async signal for {instance.name}")
    await asyncio.sleep(2)
    print(f"Async signal completed for {instance.name}")
    print(f"active signals : {threading.activeCount()}")
    
    
def t_handler(instance):
    print(f"Thread started for {instance.name}")
    import time
    time.sleep(3)
    print(f"Thread finished for {instance.name}")
    print(f"Current Thread (Threaded): {threading.get_ident()}")
    print(f"active signals : {threading.activeCount()}")
    

# Trigger Thread Signal
@receiver(post_save, sender=ThreadModel)
def trigger_thread(sender, instance, **kwargs):
    threading.Thread(target=t_handler, args=(instance,)).start()

@receiver(post_save, sender=TransactionModel)
def transaction_signal_handler(sender, instance, created, **kwargs):
    if instance.name != "Modified in Signal":
        print(f"Signal received for: {instance.name}")
        instance.name = "Modified in Signal"
        instance.save()