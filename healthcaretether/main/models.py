from datetime import datetime
from random import choice, choices
from re import M
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

#hospital model
class Hospital(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

#items model
class Items(models.Model):
    product_name = models.CharField(max_length=40)
    slug = models.SlugField(null=True, unique=True, max_length=40)

    def name(self):
        return self.product_name
    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):  # new
        if not self.id:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)

#inventory model
class Inventory(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length = 9)

    def itemName(self):
        return self.item.product_name

    def itemId(self):
        return self.item.id
    
    def __str__(self):
        return self.item.product_name
    
    def slugName(self):
        return self.item.slug


#request model
class Requests(models.Model):
    inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    requestBy = models.IntegerField()
    requestAcceptedFrom = models.IntegerField()

    def invName(self):
        return self.inventory.item

    def invQty(self):
        return self.inventory.quantity
    
    def invStatus(self):
        return self.inventory.status
    
    def invHosp(self):
        return self.inventory.hospital

    def invitemId(self):
        return self.inventory.item_id
    
    def slugName(self):
        return self.inventory.item.slug

#custom user model
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    ROLE_CHOICES = [
        ("S","Staff"),
        ("M","Manager"),
        ("A","Admin")
    ]
    role = models.CharField(max_length=1,choices = ROLE_CHOICES, default="S")

    # hospital = Hospital.objects.all()
    # HOSPITAL_CHOICES = [
    #     (1,hospital[0].name),
    #     (2,hospital[1].name),
    #     (3,hospital[2].name),
    #     (4,hospital[3].name),
    #     (5,hospital[4].name),
    #     (6,hospital[5].name),
    # ]

    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE, null=True)
    passwordChangedAt = models.DateTimeField(default = datetime.now())

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()