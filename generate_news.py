import sys

import PIL
from PIL import Image, ImageFont, ImageDraw, ImageColor

def save_image(image, orig_name, save_name):
    proper_extenction = orig_name.split('.')[-1]
    # Ensures, that save file has proper extenction
    # If not, replaces with one, from original file
    if save_name:
        if not save_name.endswith(proper_extenction):
            tmp_lst = save_name.split('.')
            tmp_lst[-1] = proper_extenction
            save_name = '.'.join(tmp_lst)
    else:
        tmp_lst = orig_name.split('.')
        tmp_lst[-2] = tmp_lst[-2] + '_news'
        save_name = '.'.join(tmp_lst)

    image.save(save_name)



def gen_news(title, subtitle, image_in, image_out=None):
    """
    Function to generate news

    :param title:     -- Main part of news
    :param subtitle:  -- Short description of news
    :param image_in:  -- path + name to file, which will be backgroundself.
                         Ideally of size 1920 by 1080. If not, will be resized
    :param image_out: -- path + name of file to save. If `None`, will be used
                         name of original file + news before *.<extenction>
    """
    # Loads background image
    image = Image.open(image_in, mode='r')
    image = image.resize((1920, 1080), Image.ANTIALIAS)

    # Create foreground dark blueish layer
    opacity = int(255 * 0.56)
    grey_img = Image.new(mode='RGBA', size=(1920, 1080), color='#1a2535')
    grey_img.putalpha(opacity)

    # Merge background with gray image
    mask = Image.new('RGBA', (1920, 1080), (0, 0, 0, opacity))
    image.paste(grey_img, mask)

    # Add mathmech logo
    logo = Image.open('images/mm-white-logo.png')
    logo = logo.resize((445, 430), Image.ANTIALIAS)
    image.paste(logo, (40, 270), logo)

    # Add title text
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/OpenSans-Regular.ttf", 115)
    draw.multiline_text((120, 650), title, (255,255,255),font=font)

    # Add subtitle text
    font = ImageFont.truetype("fonts/OpenSans-Regular.ttf", 73)
    if '\n' not in title:
        draw.multiline_text((120, 800), subtitle, (255,255,255),font=font)
    else:
        draw.multiline_text((120, 900), subtitle, (255,255,255),font=font)

    save_image(image, image_in, image_out)

if __name__ == '__main__':
    gen_news("Факультет\nВоенного обучения", "Набор сержантов запаса", "/Users/nikita/Downloads/2018-03-29 19.04.49.jpg") 
