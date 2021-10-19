import os
from PIL import Image

def openimage(arquivo):
    return Image.open(os.path.join("frames/",arquivo ))

def negativo(img:Image)-> Image:
    img_negativo = Image.new(img.mode, img.size, "blue")

    w, h = img.size
    for i in  range(w):
        for j in range(h):
            r, g, b = img.getpixel((i,j))
            img_negativo.putpixel((i,j), (255-r,255-g,255-b))
    return img_negativo

def negativo_pil():
    img = openimage('frame-001.jpg')
    negativo(img).show()
