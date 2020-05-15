'''use following script to resize images
It is command line 
Input folder must be like 
			main folder 
				subfolders
					images
					
			Example :
			raw_data ---	mainfolder
				folder_1 ---- subfolder
					image_1.png
					imag_2.png
				folder_2 ----subfolder
					image_1.png
					image_2.png
 output folder  will created automatically if not provided	
 
 subfolder names and images will remain same as input_folder in output_folder
 python resize_data.py -i input_folder location -o output_folder location -s '''
					



import argparse 
from PIL import Image 
from pathlib import Path 
import shutil 

home_location = Path.cwd()


parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',default = 'raw_Data', help = "path location of images to be resized")
parser.add_argument('-o','--output',default = 'resized',help = 'path location to save images after resize')
parser.add_argument('-H','--height',default = 224,help = 'height to be resized ')
parser.add_argument('-W','--width',default = 128,help = 'width to be resized  ')

args = parser.parse_args()


input_location = home_location /args.input
assert input_location.exists(),"Input folder location need to be check once more"
output_location = home_location / args.output


if not  output_location.exists():
    print("..................Creating output file  ...............")
    output_location.mkdir()

else:
    print("Warning:.....Removing existing folder..................")
    shutil.rmtree(output_location)
    print("............creating  folder........................")
    output_location.mkdir()

for i in input_location.iterdir():
    if i.is_dir():
        in_folder_name = i.stem
        out_path = output_location / in_folder_name
        out_path.mkdir()
        for img in i.iterdir():
            in_image_name = img.name
            image = Image.open(img).convert("RGB")
            image = image.resize((args.width,args.height))
            out_file = output_location / in_folder_name / in_image_name
            print(out_file)
            image.save(out_file)
        print("\n\n")
        print(f"Image presented in .....{in_folder_name.upper()}...... are sucessfully resized")    
        print("\n\n")       
            
    
