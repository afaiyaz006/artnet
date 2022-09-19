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

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
class SimpleImageUpload(models.Model):
        normal_image=models.ImageField(upload_to='temp_image_upload/',validators=[FileExtensionValidator(['jpg','jpeg'])])
        
class ImageUploadModel(models.Model):
        """A model for image upload form ."""
        artwork_name=models.CharField(max_length=200,default=None,help_text='Enter a artwork name')
        ordinary_image=models.ImageField(upload_to='temp',validators=[FileExtensionValidator(['jpg','jpeg'])])
        artwork_image=models.ImageField(upload_to='temp_image_upload_1/',validators=[FileExtensionValidator(['jpg','jpeg'])])
class ImageUploadModel_2(models.Model):
        """This model is used for image upload form """
        artwork_name=models.CharField(max_length=200,default=None,help_text='Enter a artwork name')
        ordinary_image=models.ImageField(upload_to='temp_image_upload_2/',validators=[FileExtensionValidator(['jpg','jpeg'])])

