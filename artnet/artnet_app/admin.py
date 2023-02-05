from django.contrib import admin
from .models import ArtWork,ArtComment,ArtStyle,Profile,BackEnd,GeneratedArtwork
# for registering model to admin 
admin.site.register(Profile)
admin.site.register(ArtWork)
admin.site.register(ArtComment)
admin.site.register(ArtStyle)
admin.site.register(BackEnd)
admin.site.register(GeneratedArtwork)
