from PIL import Image
import glob
def criar_gif():

 
# Criar frames 
    frames = []
    imgs = glob.glob("./frames/*.jpg")
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
 
    # Salvar num arquivo gif.
    frames[0].save('meu_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)