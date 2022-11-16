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
