from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

img_width = 1122
char_width = 60
max_char = 51

image_template = "D:\\Python Programs\\OpenCV\\Images\\Certificate_of_Participation.png"

name_list = ["Sriram"]

date = "06-Oct-2017"

for name in name_list:
    image = cv2.imread(image_template)
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)

    font_roboto = ImageFont.truetype("Roboto-Light.ttf", 128)

    # Write Name
    text_x = 1600 - len(name) * char_width / 2
    draw.text((text_x, 1600), name.upper(), font=font_roboto, fill=(0, 0, 0, 255))

    # Write Date
    # draw.text((810, 575), date, font=font_roboto, fill=(0, 0, 0, 255))

    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imwrite('D:\\Python Programs\\OpenCV\\' + name.upper() + ".png", cv2_im_processed)
