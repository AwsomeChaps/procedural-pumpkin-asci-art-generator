from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import requests
import sys
from PIL import Image

def main():

    html = urlopen('https://www.homemade-gifts-made-easy.com/pumpkin-coloring-pages.html')
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.png')})

    img_data = requests.get(images[random.randint(2,80)]['src']).content
    with open('pumpkin.png', 'wb') as handler:
        handler.write(img_data)
    handler.close()

    # pass the image as command line argument
    image_path = "pumpkin.png"
    img = Image.open(image_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)


if __name__ == "__main__":
    main()