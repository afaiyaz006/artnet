
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

# Creating my  views here.

def home(request):
    """
    The home of the
    webpage.
    
    """
    #loading all  artworks 
    
    artworks=ArtWork.objects.order_by("post_date")
    paginator=Paginator(artworks,5) # show 5 artworks per page
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'artnetapp/home.html',{'artworks':artworks,'page_obj':page_obj})

@login_required
def profileview(request):
    '''
    Show User profile
    '''
    artworks=ArtWork.objects.filter(author=request.user.id)
    artstyles=ArtStyle.objects.filter(art_author=request.user.id)
    
    return render(request,'artnetapp/profile.html',{'artworks':artworks,'artstyles':artstyles})

@login_required
def create_artwork_view(request):
    """Process images uploaded by users"""
    print(request.user)
    
    if request.method == 'POST':
       
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current artwork instance object to display in the template
            form_obj=form.instance
            artwork_name=form.cleaned_data['artwork_name']
            
            ordinary_image_url=form_obj.ordinary_image.path
            artwork_image_url=form_obj.artwork_image.path

            artstyle_image=form_obj.artwork_image
            
            created_artwork=process_image(ordinary_image_url,artwork_image_url)#api call need to be carefull
            user_instance = request.user
            #if 'http://' not in get_artwork_url:
            #    return render(request, 'artnetapp/artwork_creation_unsuccessfull.html')
            artwork = ArtWork()
            artstyle = ArtStyle()
            artwork.name = artwork_name
            artwork.author = user_instance
    
            if created_artwork:
                # first we are saving the style
                artstyle.art_author=user_instance
                artstyle.style_name=artwork.name+" style "
                artstyle.artStyle_image=artstyle_image
                artstyle.save()
                
                #associating artstyle with artworks
                artwork.artstyle_used=artstyle

                #saving the artwork
                artwork_file_name=str(artwork_name+".jpg")
                artwork.artwork_image.save(artwork_file_name,ContentFile(image_to_byte(created_artwork),name=artwork_file_name),save=True)
                
                return render(request, 'artnetapp/artwork_creation_successfull.html', {'artwork':artwork})
            else:
                return render(request, 'artnetapp/artwork_creation_unsuccessfull.html')
             
    else:
        form=Imageform()
        
    return render(request, 'artnetapp/artwork_create.html', {'form': form})
