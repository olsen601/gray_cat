import requests
from PIL import Image
import time
import os
import begin

cat_url = 'http://thecatapi.com/api/images/get?format=src&type=jpg'
# output_directory = 'out'

def generate_filenames(output_directory):
    name = 'cat_picture_%d.jpg' % int(time.time())
    bw_name = 'bw_' + name
    return os.path.join(output_directory, name), os.path.join(output_directory, bw_name)  # Returning a tuple of values


def download_cat_picture(filename):
    response = requests.get(cat_url)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=512):  # chunk_size is how many bytes are stored in memory at a time before writing to disk
            file.write(chunk)


def black_and_white_filter(filename, out_filename):
    image = Image.open(filename)
    bw_image = image.convert(mode='L')  # 'L' is greyscale
    bw_image.save(out_filename)


@begin.start
def main(output_dir='out'):
    try:
        filenames = generate_filenames(output_dir)
        download_cat_picture(filenames[0])
        black_and_white_filter(*filenames)  # Tuple unpacking
        print('Your cat picture is saved at %s\nThe black-and-white version is %s' % filenames) # Tuple as argument to string formatting

    except Exception as e:
        print('Error fetching image because', e)
