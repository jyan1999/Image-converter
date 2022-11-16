# Image-converter
Image format converter with Pillow. Supports converting between common image formats (JPG,PNG,HEIC,etc.) Provides a simple GUI that supports drag-and-drop multiple files.

## How it works
To use the converter, simply runs:

```bash
$ python main.py
```

And the GUI should spawn

<img width="590" alt="Image converter GUI" src="https://user-images.githubusercontent.com/49133332/202079387-90451913-2a51-4679-9bbe-5b4d49dbbb23.png">

The dropdown on the top left is the format you want to convert to. 

Simply drag and drop the image files to the designated area. The converted files will be placed in the same directory where the original images live. 

You can also click on the drag-and-drop area to browse and select files locally 

Texts in the bottom show the status of the converter and will display warnings if incompatible files are dropped. The check and output options are manually configured from [Pillow documentation](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html) and are not exhaustive. Feel free to add as long as the changes are Pillow-compatible.
