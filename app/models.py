from django.db import models
from django.contrib.auth.models import User
import uuid
from members.models import Profile


class PricingPlan(models.Model):
    PRICING_PLANS = [
        ('mobile', 'Mobile Plan'),
        ('basic', 'Basic Plan'),
        ('standard', 'Standard plan'),
        ('premium', 'Premium Plan'),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    plan_name = models.CharField(max_length=20, choices=PRICING_PLANS, default='mobile', null=True, blank=True)
    month_year = models.BooleanField(default= True)
    def __str__(self):
        return str(self.owner)