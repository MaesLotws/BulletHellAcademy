from PIL import Image

basewidth = 350
img = Image.open('Amber Angry.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('Amber Angry smol.png')
basewidth = 350 
