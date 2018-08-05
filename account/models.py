from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    token = models.CharField(max_length=255, blank=True)
    verified = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Gender of the specified entity
class Gender(models.Model):
    name = models.CharField(max_length=20, blank=False)


# Educational institute of the entity
class Institute(models.Model):
    name = models.CharField(max_length=100)