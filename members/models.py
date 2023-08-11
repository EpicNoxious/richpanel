from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  username = models.CharField(max_length=200, blank=True, null=True)
  email = models.EmailField(max_length=500, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.username)
