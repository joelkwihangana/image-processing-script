import os
from PIL import Image

input_folder="images/"
output_folder="processed/"

# Loop through file names 
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        file_path=os.path.join(input_folder,filename)
        print("Processing:",file_path)