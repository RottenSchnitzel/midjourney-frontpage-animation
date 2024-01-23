import PIL
from ascii_magic import AsciiArt
import json
import tqdm
from wand.image import Image as WandImage

all_arrays = []

def swirl_image(path):
    my_art = AsciiArt.from_image(path)
    my_art.to_terminal()
    my_art.to_file(path + ".txt")
    my_art.to_html_file(path=path + ".html")

def image_to_ascii(path):
    my_art = AsciiArt.from_image(path)
    my_art.to_terminal()
    my_art.to_file(path + ".txt")
    my_art.to_html_file(path=path + ".html")

def image_to_array(image_path, deg):
    image = PIL.Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale if necessary
    image = image.rotate(deg)
    image.thumbnail((75, 75))
    thumbnail_path = './src/lib/out.png'
    image.save(thumbnail_path)

    # Resize the image to a desired size (optional)
    # image = image.resize((width, height))

    pixels = image.load()
    width, height = image.size
    array_2d = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = pixels[x, y]
            # Check if pixel value is above a threshold (128 in this example)
            if pixel_value > 128:
                row.append(False)
            else:
                row.append(True)
        array_2d.append(row)

    return array_2d

def image_to_array2(image_path, deg):
    image = PIL.Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale if necessary
    image = image.rotate(deg)
    image.thumbnail((150, 150))
    thumbnail_path = './src/lib/out.png'
    image.save(thumbnail_path)

    # Resize the image to a desired size (optional)
    # image = image.resize((width, height))

    pixels = image.load()
    width, height = image.size
    array_2d = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = pixels[x, y]
            # Check if pixel value is above a threshold (128 in this example)
            if pixel_value > 128:
                row.append(False)
            else:
                row.append(True)
        array_2d.append(row)

    return array_2d

def save_array_to_file(array_2d, output_file):
    with open(output_file, 'w') as file:
        json.dump(array_2d, file, indent=4)

# Example usage
image_path = './src/lib/spiral.png'
image_path_logo = './src/lib/logo.png'
image_path_alcedo = './src/lib/alcedo.png'
output_file = './src/lib/out.json'
output_file_alcedo = './src/lib/alcedo.json'
image_to_ascii(image_path_logo)
for i in tqdm.tqdm(range(180)):
    all_arrays.append(image_to_array(image_path, 180 - i))
alcedo = (image_to_array2(image_path_alcedo, 0))
save_array_to_file(alcedo, output_file_alcedo)
save_array_to_file(all_arrays, output_file)