from django.urls import path
from . import views
urlpatterns = [
  path('', views.homeView, name="home"),
  path('pricing/', views.pricingView, name="pricing"),
  path('payment/', views.paymentView, name="payment"),
  path('payment/success/<str:intent_id>/<str:month_year>/<str:plan_name>/<int:price>/<str:s>/<str:e>/', views.successView, name="success"),
  path('payment/cancel/<str:intent_id>/<str:month_year>/<str:plan_name>/<int:price>/<str:s>/<str:e>/', views.cancelView, name="cancel"),
  ]
