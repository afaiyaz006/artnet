import numpy as np
import time
from artnet.settings import BASE_DIR
import PIL.Image as Image
import matplotlib.pylab as plt

import io
import tensorflow as tf
import tensorflow_hub as hub
import random

class Art:
    def __init__(self):
        print("Initialized>>>")
        self.hub_module = hub.load(str(BASE_DIR)+'\magenta_arbitrary-image-stylization-v1-256_2\\')
        self.content_image=None
        self.style_image=None
    
    def tensor_to_image(self,tensor):
        
        tensor = tensor*255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor)>3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        
        return Image.fromarray(tensor)

    def preprocess(self,content_image_path,style_image_path):
        try:
            self.content_image=Image.open(content_image_path)
        
            self.content_image=self.content_image.resize((1024,768),Image.ANTIALIAS)

            self.content_image=np.array(self.content_image)
            self.style_image=np.array(Image.open(style_image_path))

            self.content_image = self.content_image.astype(np.float32)[np.newaxis, ...]/255.
            self.style_image = self.style_image.astype(np.float32)[np.newaxis, ...] / 255.
        # Optionally resize the images. It is recommended that the style image is about
        # 256 pixels (this size was used when training the style transfer network).
        # The content image can be any size.
            self.style_image = tf.image.resize(self.style_image, (256, 256))
        except Exception as e:
            print("Error occured at preprocessing!")
    
    def process(self)->Image:
        try:
            if self.content_image is not None and self.style_image is not None:
                outputs = self.hub_module(tf.constant(self.content_image), tf.constant(self.style_image))
                stylized_image = outputs[0]
                raster_image=self.tensor_to_image(stylized_image)
                return raster_image
            else:
                return None
        except Exception as e:
            print("The following Error occured during processing!-->")
            print(f"{e}")
            return None
    

    