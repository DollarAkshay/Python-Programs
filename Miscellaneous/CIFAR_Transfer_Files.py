import os

from shutil import copyfile

CIFAR_PATH = "C:\\Users\\akshay.aradhya\\Pictures\\Data Sets\\cifar\\train\\"
DEST_PATH = "C:\\Users\\akshay.aradhya\\Pictures\\Data Sets\\cifar\\horses\\"
img_type = "horse"

file_list = os.listdir(CIFAR_PATH)

for i, file in enumerate(file_list):
    if img_type in file:
        copyfile(os.path.join(CIFAR_PATH, file), os.path.join(DEST_PATH, file))
        print(i)
