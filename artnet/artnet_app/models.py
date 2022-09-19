from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
GENDERS=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)
OCCUPATIONS=(
    ('Artist','Artist'),
    ('Student','Student'),
    ('Teacher','Teacher'),
)
class Profile(models.Model):
    """
    Model representing additional user information
    """
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    gender=models.CharField(max_length=20,choices=GENDERS,default='Male')
    occupation=models.CharField(max_length=20,choices=OCCUPATIONS,default='Artist')
    avatar_link=models.URLField(max_length=200,default='https://avatars.dicebear.com/api/adventurer-neutral/lifecouldbeadream.svg?r=50')
    



    def get_absolute_url(self):
        return reverse("user-details", args=[str(self.user.id)])


