from PIL import Image, ImageFilter

def sharpen():
    im_sharp = im.filter( ImageFilter.SHARPEN )
    name = input("What do you want to call the new file? ")
    im_sharp.save(name + '.jpg', 'JPEG' )
    r,g,b = im_sharp.split()
    exif_data = im._getexif()
    print(exif_data)
def Blur():
    im_blur = im.filter(ImageFilter.BLUR)
    name = input("What do you want to call the new file? ")
    im_blur.save(name + '.jpg', 'JPEG')
    r,g,b = im_blur.split()
    exif_data = im._getexif()
    print(exif_data)
#def InverseColours():

im = Image.open(input("File Path: "))
im.show()
a = input("What would you like to do to your image? ")
if a == 'blur':
    Blur()
elif a == 'sharpen':
    sharpen()



