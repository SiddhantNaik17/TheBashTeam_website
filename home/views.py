from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from products.models import Product
from util import dialogflow

df = dialogflow.DialogFlow()


class HomepageView(View):
    def get(self, request):
        trending_products = Product.objects.filter(active=True, trending=True)

        context = {
            'trending_products': trending_products,
        }
        return render(request, 'home/index.html', context)


@csrf_exempt
def bot_message(request):
    message = request.POST['message']
    response = df.detect_intent_texts(message)
    return JsonResponse({
        'messages': [message.text.text[0] for message in response.query_result.fulfillment_messages]
    })
