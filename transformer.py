import numpy as np
import pandas as pd
import os
from PIL import Image
from PIL import UnidentifiedImageError
import shutil

def process_img(fp):
    with Image.open(fp) as img:
        img = img.crop((11, 8, 71, 68))
        img = img.convert(mode="L")
        img_data = np.asarray(img)
        return img_data

blank_data = process_img(r"blank_compass.png")
aggregate_data = np.zeros((60, 60), dtype=int)
for fp in os.listdir("data"):
    try:
        img_data = process_img(f"data/{fp}")
        diff = img_data - blank_data
        if np.sum(diff) < 100000:
            shutil.copyfile(f"data/{fp}", f"sapply/{fp}")
            diff[diff < 20] = 0
            diff[diff >= 20] = 1
            aggregate_data += diff
    except UnidentifiedImageError:
        print(f"Image {fp} error")

df = pd.DataFrame(aggregate_data)
df.to_csv("sapply.csv")