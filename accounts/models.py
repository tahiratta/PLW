from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
        is_lender = models.BooleanField(default=False)
        is_borrower = models.BooleanField(default=False)
        address = models.CharField(max_length=255, default='', blank=True, )
class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    credit_rating = models.CharField(max_length=255, default='',blank=True,unique=False)
    sscard = models.CharField(max_length=255, default='',blank=True,unique=False)


    def __str__(self):
        return self.user.username


class Lender(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    entity_name = models.CharField(max_length=255,default='',blank=True)
    available_funds = models.CharField(max_length=255, default='',null=True, blank=True)
    loan_range = models.CharField(max_length=255, default='',null=True, blank=True)
    min_loan_size = models.CharField(max_length=255, default='',null=True, blank=True)
    max_loan_size = models.CharField(max_length=255, default='',null=True, blank=True)
    min_credit = models.CharField(max_length=255, default='',null=True, blank=True)
    max_ltv = models.CharField(max_length=255, default='',null=True, blank=True)
    max_ltc = models.CharField(max_length=255, default='',null=True, blank=True)
    states = models.CharField(max_length=255, default='',null=True, blank=True)
    property_type = models.CharField(max_length=255, default='',null=True, blank=True)
    foreclosure = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
