import cv2
import sys
import os.path

def get_image_path():
    # If argv is present, file exists and is image
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        formats = ['png', 'jpg', 'jpeg', 'gif']
        extension = image_path.split('.')[1]

        if os.path.isfile(image_path) and extension in formats:
            return sys.argv[1]
        else:
            return None
    else:
        return None

def get_scale():
    # If argv is present, scale exists and is number
    if len(sys.argv) > 2:        
        scale = sys.argv[2]

        try:
            scale = float(scale)
            return scale
        except:
            return 1
    else:
        return 1

def get_size(image, scale):
    # Get image size after scale
    width, height, channels = image.shape

    return int(width * scale), int(height * scale)

def check_image_path(image_path):
    # Checks if image path is None
    if image_path == None:
        print('Invalid image path (parameter 0). Exiting...')
        exit()

def get_ascii(image):
    # Transforms image to ASCII
    ascii_image = []
    luminosity_array = ' .:-=+*#%@'
    width, height, channels = image.shape

    for x in range(width):
        ascii_image.append([])

        for y in range(height):
            ascii_image[x].append([])

            # Converts to greyscale
            color = image[x][y]
            luminosity = sum(color)/3

            # Index goes from 0 to len(luminosity_array) based on luminosity
            ascii_image[x][y] = luminosity_array[int((luminosity/255) * (len(luminosity_array) - 1))]

    return ascii_image

def print_ascii_image(ascii_image):
    # Prints characters in ASCII image
    for row in ascii_image:
        for val in row:
            print(val, end = ' ')
        
        print()

def main():
    image_path = get_image_path()
    check_image_path(image_path)
    image = cv2.imread(image_path)
    
    scale = get_scale()
    width, height = get_size(image, scale)
    image = cv2.resize(image, (width, height))

    ascii_image = get_ascii(image)
    print_ascii_image(ascii_image)

if __name__ == '__main__':
    main()