import PIL
from PIL import Image

text_chars = ["@", "0", "#", "S", "%", "?", "*", "+", "=", ";", ":", "-", ",", "."]

def gray_it_out(image):
    gray_image = image.convert("L")
    return(gray_image)

def resize_image(image, updated_width=100):
    width, height = image.size
    ratio = height/width * 0.5
    updated_height = int(updated_width * ratio)
    resized_image = image.resize((updated_width, updated_height))
    return(resized_image)

def pixels_to_text(image):
    pixels = image.getdata()
    characters = "".join([text_chars[pixel//25] for pixel in pixels])
    return(characters)


def convert(updated_width=100):
    path = input("Enter a valid pathname to an image:\n")

    try:
        image = PIL.Image.open(path)

    except:
        print(f"{path} is an invalid path. Try the exact path to your image\n")


    new_file_name = input("Enter the file name to save this image to:\n")

    new_data = pixels_to_text(gray_it_out(resize_image(image)))

    pixel_count = len(new_data)
    text_image = "\n".join([new_data[index:(index+updated_width)] for index in range(0, pixel_count, updated_width)])

    # print(text_image)
    with open(f"/Users/kenttaylor/Desktop/{new_file_name}.text", "w") as file:
        file.write(text_image)

convert()