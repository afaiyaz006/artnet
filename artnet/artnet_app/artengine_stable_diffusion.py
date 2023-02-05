from .models import BackEnd
import PIL.Image as Image
import requests
from io import BytesIO
import base64

class CreateArt:
    """
        This class helps to connect with the backend of 
        Stable diffusion and get the image that is requested.
        Jor koira class Banaisi uWu
    """
    def __init__(self,text:str):
        self.text=text
        self.backend_url=BackEnd.objects.all()[0].back_end_url
    
    def decode_image(self,img_str):
        img_bytes=base64.b64decode(img_str)
        img=Image.open(BytesIO(img_bytes))
        return img
    
    def process(self):
        try:
            request_url=self.backend_url+'/get_image/'+self.text

            data=requests.get(request_url)
    
            final_image=self.decode_image(data.text)
            return final_image
        except:
            return None