from django import forms
from django.forms import ModelForm
from .models import PricingPlan

class PricingPlanForm(ModelForm):
    plan_name = forms.ChoiceField(
        choices=PricingPlan.PRICING_PLANS,
        widget=forms.RadioSelect()
    )
    class Meta:
        model = PricingPlan
        fields = ['month_year', 'plan_name']
        labels = {'month_year':'Month/Year','plan_name': 'select pricing plan'}