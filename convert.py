from PIL import Image
from pillow_heif import register_heif_opener
import os 

register_heif_opener()
    
def convert(url, target):
    im = Image.open(url)
    splitted = os.path.splitext(url)[0]
    if target != "HEIC":
        target = target.lower()
    combined = "{}.{}".format(splitted,target)
    im.save(combined)

    
def acceptable(urls, supported_inputs):
    for url in urls:
        extension = os.path.splitext(url)[1][1:]
        if extension.lower() not in supported_inputs:
            return False 
    return True
