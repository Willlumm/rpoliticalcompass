import numpy as np
from PIL import Image

def process_img(path):
    with Image.open(path) as img:
        img = img.crop((11, 8, 71, 68))
        img = img.convert(mode="L")
        img_data = np.asarray(img)
        return img_data

def display(img):
    output = ""
    for row in img:
        for n in row:
            output += str(n)
        output += "\n"
    print(output)
    
blank = process_img(r"blank_compass.png")
compass = process_img(r"data\1662142130_5.png")
diff = np.abs(compass - blank)
diff[diff > 0] = 1
display(diff)


