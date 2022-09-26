import numpy as np
from PIL import Image

with Image.open(r"data\1662142130_5.png") as img:
    img = img.crop((10, 8, 70, 68))
    img = img.convert(mode="L")
    img.show()
    img_data = np.asarray(img)
    print(img_data)