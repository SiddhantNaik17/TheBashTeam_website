from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from billing.utils import initiate_transaction

PAYTM_MERCHANT_ID = 'SNeEfa79194346659805'
PAYTM_MERCHANT_KEY = 'T7V3cbVmVIN1#YK7'


def initiate(request):
    order_id = request.session['order_id']
    response = initiate_transaction(order_id)
    context = {
        'mid': PAYTM_MERCHANT_ID,
        'order_id': order_id,
        'txn_token': response['body']['txnToken'],
    }
    return render(request, 'billing/show_payments.html', context)


@csrf_exempt
def processing(request):
    return render(request, 'billing/transaction_in_process.html')
