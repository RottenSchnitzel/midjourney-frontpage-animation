import PIL
from ascii_magic import AsciiArt
from bs4 import BeautifulSoup
import html
import json
import os
import tqdm
import random
from wand.image import Image as WandImage
from wand.color import Color

all_arrays = []

from wand.image import Image as WandImage
import tqdm

def zoom_image(img, zoom_factor):
	original_width, original_height = img.width, img.height

	new_width = int(original_width / zoom_factor)
	new_height = int(original_height / zoom_factor)

	left = (original_width - new_width) // 2
	top = (original_height - new_height) // 2
	right = left + new_width
	bottom = top + new_height

	img.crop(left=left, top=top, right=right, bottom=bottom)

	return img

def swirl_image(degree, img, zoom_factor):
	img.swirl(degree=-degree)
	img = zoom_image(img, zoom_factor)

	return img

def swirl_animate(path, out_path):
	with WandImage(filename=path) as original_img:
		current_zoom_factor = 1.0

		for i in tqdm.tqdm(range(total_iterations)):
			img = WandImage(original_img)  # Create a copy of the original image for each iteration
			img = swirl_image(degree=i, img=img, zoom_factor=current_zoom_factor)
			img.save(filename=out_path + "logo_swirl_" + str(i) + ".png")

			# Increase the zoom factor for the next iteration
			current_zoom_factor += zoom_increment

def image_to_ascii(path):
	my_art = AsciiArt.from_image(path)
	#my_art.to_terminal()
	my_art.to_file(path + ".txt", monochrome=True)
	#my_art.to_html_file(path=path + ".html", columns=80)
	
def process_html_file(file_path):
	with open(file_path, 'r') as file:
		soup = BeautifulSoup(file, 'html.parser')
		pre_tag = soup.find('pre')

		if pre_tag:
			return str(pre_tag)
		else:
			return None
		
def process_text_file(file_path):
	out = ""
	with open(file_path, 'r') as file:
		lines = file.readlines()
	for line in lines:
		out = out + line
	return html.escape(out)

def process_text_file_lines(file_path):
	out = []
	with open(file_path, 'r') as file:
		lines = file.readlines()
	for line in lines:
		out.append(html.escape(line))
	return out

def animations_to_ascii_to_array(input_folder,output_file):
	json_array = []
	json_array_text = []
	json_array_text_array = []
	for i in tqdm.tqdm(range(total_iterations)):
		image_to_ascii(input_folder + "logo_swirl_" + str(i) + ".png")
		#html = process_html_file(input_folder + "logo_swirl_" + str(i) + ".png.html")
		#if html:
		#	json_array.append(html)
		text = process_text_file(input_folder + "logo_swirl_" + str(i) + ".png.txt")
		if text:
			json_array_text.append(text)
		text_array = process_text_file(input_folder + "logo_swirl_" + str(i) + ".png.txt")
		if text_array:
			json_array_text_array.append(text_array)
	with open(output_file + ".html.json", 'w') as json_file:
		json.dump(json_array, json_file, indent=2)
	with open(output_file + ".txt.json", 'w') as json_file:
		json.dump(json_array_text, json_file, indent=2)
	with open(output_file + ".array.json", 'w') as json_file:
		json.dump(json_array_text_array, json_file, indent=2)


image_path = './src/lib/logo/logo.png'
image_output_folder = './src/lib/logo/'
output_folder = './src/lib/'
total_iterations = 1000
zoom_increment = 0.005
image_to_ascii(image_path)
swirl_animate(image_path, image_output_folder + "animated/")
animations_to_ascii_to_array(input_folder=image_output_folder+"animated/", output_file=output_folder+"logo")