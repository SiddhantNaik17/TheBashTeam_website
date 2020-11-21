import uuid

import requests
import json

from django.urls import reverse_lazy
from paytmchecksum import PaytmChecksum

from orders.models import Order

PAYTM_MERCHANT_ID = 'SNeEfa79194346659805'
PAYTM_MERCHANT_KEY = 'T7V3cbVmVIN1#YK7'


def initiate_transaction(order_id):
    order = Order.objects.get(id=order_id)
    paytmParams = dict()

    paytmParams['body'] = {
        'requestType': 'Payment',
        'websiteName': 'WEBSTAGING',
        'mid': PAYTM_MERCHANT_ID,
        'orderId': order.id,
        'callbackUrl': 'http://127.0.0.1:8000' + str(reverse_lazy('processing')),
        'txnAmount': {
            'value': float(order.total),
            'currency': 'INR',
        },
        'userInfo': {
            'custId': order.user.id if order.user else str(uuid.uuid4()),
        },
    }

    # Generate checksum by parameters we have in body
    checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams['body']), PAYTM_MERCHANT_KEY)

    paytmParams['head'] = {
        'signature': checksum
    }

    post_data = json.dumps(paytmParams)

    # for Staging
    url = f"https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid={PAYTM_MERCHANT_ID}&orderId={order.id}"

    # for Production
    # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"

    response = requests.post(url, data=post_data, headers={'Content-type': 'application/json'}).json()
    return response  # Todo: Handle failures
