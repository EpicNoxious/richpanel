from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import PricingPlan
from .forms import PricingPlanForm
from django.urls import reverse
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_PRIVATE_KEY
import time
from datetime import datetime, timedelta

def homeView(request):
  context= {}
  return render(request, 'index.html', context)


def pricingView(request):
    profile = request.user.profile
    pricing_plan, created = PricingPlan.objects.get_or_create(owner=profile)
    if request.method == 'POST':
      form = PricingPlanForm(request.POST, instance=pricing_plan)
      if form.is_valid():
        form.save()
        return redirect('payment')
    else:
       form = PricingPlanForm(instance=pricing_plan)   
    
    context = {'profile': profile, 'form': form}
    return render(request, 'pricing.html', context)

def paymentView(request):
  profile = request.user.profile
  pricing_plan = PricingPlan.objects.get(owner=profile)
  month_year = pricing_plan.month_year
  plan_name = pricing_plan.plan_name
  context = {}
  PRICE = {
        'mobile': 100,
        'basic': 200,
        'standard': 500,
        'premium': 700,
    }
  price = PRICE.get(plan_name, 0) if  month_year else PRICE.get(plan_name, 0) * 10
  intent = stripe.PaymentIntent.create(
    amount=price,
    currency="inr",
    payment_method_types=["card"],
    metadata={"integration_check": "accept_a_payment"},
  ) 
  current_date = datetime.now()
  if(month_year == True): 
    num = 30
  else: 
    num = 365
  future_date = current_date + timedelta(days=num)
  s = current_date.strftime('%d-%m-%Y')
  e = future_date.strftime('%d-%m-%Y')
  context = {'month_year': month_year, 'plan_name': plan_name, 'price':price, 'client_secret':intent.client_secret, 'profile': profile.username, 's':s, 'e': e}
  
  if request.method == 'POST':
    intent_id = intent.get('id')
    time.sleep(5)
    return redirect('success', intent_id=intent_id, month_year=month_year, plan_name=plan_name, price=price, s=s, e=e)
  
  return render(request, 'payment.html', context)

def successView(request, intent_id, month_year, plan_name, price, s, e):
  if request.method == 'POST':
    return redirect('cancel', intent_id=intent_id, month_year=month_year, plan_name=plan_name, price=price, s=s, e=e)
  context = {'intent_id': intent_id,'month_year': month_year, 'plan_name': plan_name, 'price':price,'s':s, 'e': e}
  return render(request, 'success.html', context)

def cancelView(request, intent_id, month_year, plan_name, price, s,e):
  intent = stripe.PaymentIntent.retrieve(intent_id)
  intent.cancel()
  context = {'intent_id': intent_id,'month_year': month_year, 'plan_name': plan_name, 'price':price,'s':s, 'e': e}
  return render(request, 'cancel.html', context)