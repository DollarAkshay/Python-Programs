from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

img_width = 1122
char_width = 22
max_char = 51

image_template = "C:\\Users\\akshay.aradhya\\Pictures\\Graphic Design\\SwiftCode Certificates\\SwiftCode Certificate Template.png"

name_list = ["Abhishek Harsh", "Akanksha Kumari", "Animesh Singh", "Deepak V Kashyap ", "Hardik Asnani",
             "Kailasa Aravind", "Kashyap Kitchlu", "Macha Pujitha", "Magadal Shriya", "Nagarjun  T N ", "Navneeth Kumar",
             "Rashmi N", "Sanjna Umesh", "Sankarshan A Joshi", "Sharath S K", "Shubhangi Vasishta", "Suhaib Khan", "Supriya M",
             "Christeen S", "Raksha A"]

date = "06-Oct-2017"

for name in name_list:
    image = cv2.imread(image_template)
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)

    font_courbd = ImageFont.truetype("courbd.ttf", 36)
    font_roboto = ImageFont.truetype("Roboto-Light.ttf", 24)

    # Write Name
    draw.text(((max_char - len(name)) * char_width / 2, 370),
              name.upper(), font=font_courbd, fill=(0, 0, 0, 255))

    # Write Date
    draw.text((810, 575), date, font=font_roboto, fill=(0, 0, 0, 255))

    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imwrite('C:\\Users\\akshay.aradhya\\Pictures\\Graphic Design\\SwiftCode Certificates\\BNMIT\\' +
                name.upper() + ".png", cv2_im_processed)
