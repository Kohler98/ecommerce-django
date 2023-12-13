import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.conf import settings
from basket.models import Basket
from orders.views import payment_confirmation
# Create your views here.
def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')
class Error(TemplateView):
    template_name = 'payment/error.html'

@login_required
def basketView(request):
    
    basket = Basket(request)
    
    total = str(basket.get_subtotal_price())
    total = total.replace('.','')
    total = int(total)
    
    stripe.api_key = settings.SECRET_KEY
    

    intent = stripe.PaymentIntent.create(
        amount=total,
        currency="usd",
        metadata={'userid':request.user.id}
    )
    return render(request,'payment/home.html', {'client_secret':intent.client_secret})    

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
         
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
 
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print(f'Unhandled event type {event.type}')

    return HttpResponse(status=200)