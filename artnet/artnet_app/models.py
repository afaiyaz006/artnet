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

IS_FAMOUS=(
    ('Yes','Yes'),
    ('No','No')
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
    
class ArtStyle(models.Model):
    """
    Model representing art style collections.
    """
    art_author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    style_name=models.CharField(max_length=200)
    artStyle_image=models.ImageField(upload_to='artstyle_images/',validators=[FileExtensionValidator(['jpg','jpeg'])])
    
    is_famous=models.CharField(max_length=50,choices=IS_FAMOUS,default="No",null=True)

    def __str__(self):
        return self.style_name
    def get_absolute_url(self):
        """
        Returns the url to access a particular Artwork instance.
        """
        return reverse('artstyle-detail', args=[str(self.id)])
    
class ArtWork(models.Model):
    """
    Model representing a ArtWork
    """
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    artstyle_used=models.ForeignKey(ArtStyle,on_delete=models.CASCADE,null=True)
    artwork_image=models.ImageField(upload_to='artwork_images/')
    
    post_date = models.DateField(default=date.today)
    likes = models.ManyToManyField(User,blank=True,related_name='collected_likes')
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular Artwork instance.
        """
        return reverse('artwork-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name   
    
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

class TextPromptModel(models.Model):
    """
        This model is used for collecting text prompt
    """
    prompt=models.TextField(max_length=200,default=None,help_text='Enter a what you want to draw.')



class ArtComment(models.Model):
    """
    Model representing a comment against a Artpost.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about the art here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because ArtComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    artwork= models.ForeignKey(ArtWork, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=60
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring

class GeneratedArtwork(models.Model):
    """
        Model for storing generated artwork
    """    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prompt=models.TextField(max_length=500,help_text="Type Your Artwork Prompt here.")
    artwork_image=models.ImageField(upload_to='artwork_images/')


class BackEnd(models.Model):
    back_end_url=models.URLField(max_length=1000)