from PIL import ImageFont, ImageDraw, Image
import time
import os
import cv2
import numpy as np

img_width = 1122
char_width = 22
max_char = 51

folder_path = "C:\\Users\\akshay.aradhya\\Pictures\\Graphic Design\\SwiftCode Receipts\\SJBIT\\"

name_list = ["ABHINAV A BHOPARDIKAR", "AISHWARYA PADMANABHA", "AJAY G", "AKASH K S",
             "AKSHATHA R BHAT", "AMRUTHA VARSHINI B.K", "ANAGHA RAGHVENDRA DUDIHALLI", "ANANYA I.R",
             "ASHISH KUMAR M S", "BONAGIRI SRI PRANATHI", "KARTHIK B R", "KARTHIK M", "KHAWJA GHOUSE",
             "N R SWARAS", "NISHANTH R DEVAGIRI", "POOJA G", "PRADNYA DATTATRAY PATIL", "SHARADHI N",
             "SHASHANK R", "SHASHANK.G.S", "SHASHIDHARA G", "SIDDESH ANGADI", "SUHAS G", "SUJAN K S",
             "SUPRITHA P", "TOUFEEQ ULLA KHAN", "VINODA RAJU G M", "AISHWARYA S", "CHITHRA R.M",
             "KAVANA N BHATT", "SMRITI PRABHA", "SREEVATS R RAVILLU", "SUPRIYA", "SWETHA.B.S",
             "VANITHA R", "VISHALAKSHI R", "VISHWAL P K", "NIKHIL D", "SACHIN.M", "SHRAAVYA K", "RUCHIKA SINGHI"]

college_name = "SJBIT"
date = "14/09/2017"
receipt_no = "20170914-"

for i, name in enumerate(name_list):

    image = cv2.imread(
        "C:\\Users\\akshay.aradhya\\Pictures\\Graphic Design\\Betsol SwiftCode Receipt.png")
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)
    font = ImageFont.truetype("Roboto-Regular.ttf", 50)

    draw.text((270, 807),
              name, font=font, fill=(33, 33, 33, 255))
    draw.text((290, 872),
              college_name, font=font, fill=(33, 33, 33, 255))
    draw.text((1330, 807),
              receipt_no + ("{:03d}".format(i)), font=font, fill=(33, 33, 33, 255))
    draw.text((1200, 872),
              date, font=font, fill=(33, 33, 33, 255))

    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    cv2.imwrite(folder_path + name + ".png", cv2_im_processed)


time.sleep(5)

print("Combining")

if not os.path.exists(folder_path + "combined"):
    os.makedirs(folder_path + "combined")

k = 0
img1 = None
img2 = None
file_list = os.listdir(folder_path)


for file in file_list:
    if file != 'combined':
        if img1 is None:
            img1 = cv2.imread(folder_path + file)
        elif img2 is None:
            img2 = cv2.imread(folder_path + file)
            combined = np.concatenate((img1, img2), axis=1)
            cv2.imwrite(folder_path + "combined\\" + str(k) + ".png", combined)
            k += 1
            img1 = None
            img2 = None

if img1 is not None:
    cv2.imwrite(folder_path + "combined\\" + str(k) + ".png", img1)
    k += 1
