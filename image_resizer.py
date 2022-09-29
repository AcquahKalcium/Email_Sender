# install pillow
# import image
# open up the image we want to resize using Python
# print the current size of that image
# specify the size toc change it to
# save the new resized image

from PIL import Image

def resize_image(size1, size2):

    image = Image.open('men.jpg.jpg')

    print(f"current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('men.jpg' + str(size1) + '.jpg')

size1 = int(input('Enter width: '))
size2 = int(input('Enter lenght: '))
resize_image(size1, size2)


