from django.db import models
# Import lib for phone number field
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# Services types table
class ServicesType(models.Model):

    services_name = models.CharField(max_length=50)

    # How it will be printed in Shell or Django admin
    def __str__(self):
        return self.services_name


# Business cards table
class BusinessCard(models.Model):

    company_name = models.CharField(max_length=128, null=False)
    # Services type foreign key
    services_type = models.ForeignKey("ServicesType", on_delete=models.CASCADE)
    description = models.TextField()
    phone_number = PhoneNumberField(null=False, blank=False)
    instagram = models.CharField(max_length=128, blank=True)
    telegram = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128)
    website = models.CharField(max_length=128, blank=True)

    # How it will be printed in Shell or Django admin
    def __str__(self):
        return f'"{self.company_name}"'
