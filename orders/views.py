from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def order_confirmed(request):
    return render(request, 'orders/confirmed.html')
