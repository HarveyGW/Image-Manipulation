from colorama import Fore; from PIL import Image, ImageFilter, ImageSequence; import PIL.ImageOps; import re #Imports

#Sharpen
def Sharpen():
    im_sharp = im.filter( ImageFilter.SHARPEN )
    name = input("What do you want to call the new file? ")
    ext = input("What is the file extension: ")
    if ext == '.jpg':
        j = "JPEG"
    elif ext == '.png':
        j = "PNG"
    try:
        im_sharp.save(name + ext, j )
        print(Fore.LIGHTGREEN_EX + "Done")
    except:
        print(Fore.LIGHTRED_EX + "Failed")

#Blur
def Blur():
    im_blur = im.filter(ImageFilter.BLUR)
    name = input("What do you want to call the new file? ")
    ext = input("What is the file extension: ")
    if ext == '.jpg':
        j = "JPEG"
    elif ext == '.png':
        j = "PNG"
    try:
        im_blur.save(name + ext, j )
        print(Fore.LIGHTGREEN_EX + "Done")
    except:
        print(Fore.LIGHTRED_EX + "Failed")

#ExtractingFrames
def ExtractingFrames():
    index = 1
    try:
        for frame in ImageSequence.Iterator(im):
            frame.save("frame%d.png" % index)
            index += 1
        print(Fore.LIGHTGREEN_EX + "Done")
    except:
        print(Fore.LIGHTRED_EX + "Failed")

#Invert Colours
def InvertColours():
    s = FilePath.split('.')
    if "jpg" in s:
        try:
            im_Invert = PIL.ImageOps.invert(im)
            name = input("What do you want to call the new file? ")
            ext = input("What is the file extension: ")
            if ext == '.jpg':
                j = "JPEG"
            elif ext == '.png':
                j = "PNG"
            try:
                im_Invert.save(name + ext, j )
                print(Fore.LIGHTGREEN_EX + "Done")
            except:
                print(Fore.LIGHTRED_EX + "Failed")
        except:
            print(Fore.LIGHTRED_EX + "Failed")
    else:
        print(Fore.LIGHTRED_EX + "INVALID FILE FORMAT (JPEG ONLY)")

FilePath = input("File Path: ")
im = Image.open(FilePath)
im.show()
a = input("Choose (blur, sharpen, extract, invert): ")
if a == 'blur':
    Blur()
elif a == 'sharpen':
    Sharpen()
elif a == 'extract':
    ExtractingFrames()
elif a == 'invert':
    InvertColours()

