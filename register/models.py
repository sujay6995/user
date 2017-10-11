from django.db import models
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
# Create your models here.

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User)
  portfolio = models.URLField(blank=True)
  picture = models.ImageField(upload_to= 'profile_pictures',blank=True)

  def __str__(self):
      return self.User.Username


