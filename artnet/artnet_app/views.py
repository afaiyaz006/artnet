
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .artengine import process_image,image_to_byte
from artnet_app.forms import Imageform,ArtWork_with_selected_artstyle_form, SignupForm,ArtStyleForm
from .models import ArtComment, ArtWork,ArtStyle,SimpleImageUpload,Profile
from django.core.files.base import ContentFile
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render,redirect
from .forms import SignupForm,ArtWork_with_Famous_ArtStyle
from django.core.paginator import Paginator
