import os
from PIL import Image

input_folder="images/"
output_folder="processed/"

# Loop through file names 
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        file_path=os.path.join(input_folder,filename)
        print("Processing:",file_path)
        with Image.open(file_path) as img:
            rotated=img.rotate(-90) # -90 clocckwise rotation
            #the second requirement is resizing.
            resized=rotated.resize((128,128)) #.resize((width,height))->create a new sized image
            #save in Correct Format
            new_filename=os.path.splitext(filename)[0] + ".jpg"
            save_path=os.path.join(output_folder,new_filename)
            resized.save(save_path,"JPEG")
            print("Saved:",save_path)