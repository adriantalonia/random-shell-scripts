from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User
from common.models import (
  CommonFields,
  Address,
  City
)
from common.validators import ModelValidators

# Create your models here.

class UserAddress(Address):
  user = models.ForeignKey (
    User,
    null = False,
    blank = False,
    on_delete = models.CASCADE
  )
  city = models.ForeignKey (
    City,
    related_name = 'user_city_address',
    null = True,
    blank = True,
    on_delete = models.CASCADE
  )

  def __str__(self):
    return self.alias

  class Meta:
    verbose_name = "User address"
    verbose_name_plural = "User address'"

  class JSONAPIMeta:
    resource_name = "UserAddress"

languages = (
  ('EN', 'English'),
  ('ES', 'Español')
)
currency = (
  ('USD', 'USD'),
  ('MXP', 'MXP')
)

class UserProfile(CommonFields):
  user = models.ForeignKey (
    User,
    null = False,
    blank = False,
    on_delete = models.CASCADE
  )
  language = models.CharField (
    max_length = 2,
    choices = languages,
    default = 'EN',
    null = True,
    blank = True
  )
  currency = models.CharField (
    max_length = 3,
    choices = currency,
    default = 'USD',
    null = True,
    blank = True
  )
  newsletter = models.BooleanField (
    default=False,
    blank=False,
    null=False
  )
  promotions = models.BooleanField (
    default=False,
    blank=False,
    null=False
  )

  def __str__(self):
    return self.user.first_name

  class Meta:
    verbose_name = "User profile"
    verbose_name_plural = "User profiles"

  class JSONAPIMeta:
    resource_name = "UserProfile"
