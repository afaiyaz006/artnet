from django import forms
from .models import ImageUploadModel, ImageUploadModel_2,ArtStyle
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

class ArtWork_with_selected_artstyle_form(forms.ModelForm):
    """
        Form for the upload model of artwork with selected artstyle
    """
    class Meta:
        model=ImageUploadModel_2
        fields=('artwork_name','ordinary_image')