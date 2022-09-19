
from artnet.settings import BASE_DIR
from .artengine_tensorflow import Art
import PIL.Image as Image
import io


def process_image(content_image_path, style_image_path)->Image:
    artmaker=Art()
   
    #print(f"Content Image Path: {content_image_path}, Style image path {style_image_path}")
    try:
        artmaker.preprocess(content_image_path,style_image_path)
        created_artwork=artmaker.process()
        return created_artwork
    except Exception as e:
        print(f"{e}")


def image_to_byte(image: Image) -> bytes:

    buffer=io.BytesIO()
    image.save(buffer,format='JPEG')
    byte_image=buffer.getvalue()
    return byte_image