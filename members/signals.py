from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from app.models import PricingPlan
from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
  if created:
    user = instance
    profile = Profile.objects.create(
      user = user,
      username = user.username,
      email = user.email,
    )

    # subject = 'Welcome to Wordle'
    # message = 'We glad you are here'

    # send_mail(
    #   subject,
    #   message,
    #   settings.EMAIL_HOST_USER,
    #   [profile.email],
    #   fail_silently=False,
    # )
def createPricingPlan(sender, instance, created, **kwargs):
  if created:
    user = instance
    plan = PricingPlan.objects.create(owner = user)


def deleteProfile(sender, instance, **kwargs):
  try:
    user = instance.user
    user.delete()
  except:
    pass

  
def updateUser(sender, instance, created, **kwargs):
  if created:
    profile = instance
    user = profile.user
    if created == False:
      user.username = profile.username
      user.email = profile.email
      user.save()

post_save.connect(createProfile, sender=User)
post_save.connect(createPricingPlan, sender=Profile)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)