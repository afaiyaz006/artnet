from django import forms
from .models import ImageUploadModel, ImageUploadModel_2,ArtStyle,TextPromptModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GENDERS,OCCUPATIONS
class SignupForm(UserCreationForm):
    """
        Form for handaling signups
    """
    gender =forms.ChoiceField(choices=GENDERS,widget=forms.RadioSelect,initial='Male')
    occupation = forms.ChoiceField(choices=OCCUPATIONS,initial='Artist')
    class Meta:
        model=User
        fields=('username','first_name','last_name','gender','occupation','email','password1','password2')

class Imageform(forms.ModelForm):
    """
    Form for the image model
    """
    class Meta:
        model=ImageUploadModel
        fields=('artwork_name','ordinary_image','artwork_image')

class TextPromptForm(forms.ModelForm):
    """
        Form for text prompt of ai generated
    """
    class Meta:
        model=TextPromptModel
        fields=('__all__')
class ArtWork_with_selected_artstyle_form(forms.ModelForm):
    """
        Form for the upload model of artwork with selected artstyle
    """
    class Meta:
        model=ImageUploadModel_2
        fields=('artwork_name','ordinary_image')

class ArtWork_with_Famous_ArtStyle(forms.Form):
    """
        Form for creating artwork with famous artstyle
    """
    artwork_name=forms.CharField(max_length=100)
    famous_artstyle=forms.ModelChoiceField(queryset=ArtStyle.objects.filter(is_famous='Yes'))
    ordinary_image=forms.ImageField()

class ArtStyleForm(forms.ModelForm):
    
    class Meta:
        model=ArtStyle
        fields=('style_name','artStyle_image')