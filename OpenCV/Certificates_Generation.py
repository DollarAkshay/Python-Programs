from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np

img_width = 1122
char_width = 22
max_char = 51

name_list = ["ABHINAV A BHOPARDIKAR", "AISHWARYA PADMANABHA", "AJAY G", "AKASH K S",
             "AKSHATHA R BHAT", "AMRUTHA VARSHINI B.K", "ANAGHA RAGHVENDRA DUDIHALLI", "ANANYA I.R",
             "ASHISH KUMAR M S", "BONAGIRI SRI PRANATHI", "KARTHIK B R", "KARTHIK M", "KHAWJA GHOUSE",
             "N R SWARAS", "NISHANTH R DEVAGIRI", "POOJA G", "PRADNYA DATTATRAY PATIL", "SHARADHI N",
             "SHASHANK R", "SHASHANK.G.S", "SHASHIDHARA G", "SIDDESH ANGADI", "SUHAS G", "SUJAN K S",
             "SUPRITHA P", "TOUFEEQ ULLA KHAN", "VINODA RAJU G M", "AISHWARYA S", "CHITHRA R.M",
             "KAVANA N BHATT", "SMRITI PRABHA", "SREEVATS R RAVILLU", "SUPRIYA", "SWETHA.B.S",
             "VANITHA R", "VISHALAKSHI R", "VISHWAL P K", "NIKHIL D", "SACHIN.M", "SHRAAVYA K", "RUCHIKA SINGHI"]

for name in name_list:
    image = cv2.imread("OpenCV/images/SwiftCode Certificate.png")
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)
    font = ImageFont.truetype("courbd.ttf", 36)
    draw.text(((max_char - len(name)) * char_width / 2, 370),
              name, font=font, fill=(0, 0, 0, 255))
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    cv2.imwrite('C:\\Users\\akshay.aradhya\\Pictures\\Graphic Design\\SwiftCode Certificates\\' +
                name + ".png", cv2_im_processed)
