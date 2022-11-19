import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from PIL import Image
from PIL import UnidentifiedImageError
import seaborn as sns
import shutil

def process_img(fp):
    with Image.open(fp) as img:
        img = img.crop((11, 8, 71, 68))
        img = img.convert(mode="L")
        img_data = np.asarray(img)
        # img_data = np.ravel(img_data)
        return img_data

def display(img):
    output = ""
    for row in img:
        for n in row:
            output += str(n)
        output += "\n"
    print(output)

blank_data = process_img(r"blank_compass.png")
aggregate_data = np.zeros((60, 60), dtype=int)
count = 0
ignored = 0
# for fp in os.listdir("data"):
for fp in os.listdir("sapply"):
    try:
        img_data = process_img(f"data/{fp}")
        diff = img_data - blank_data
        if np.sum(diff) < 100000:
            # shutil.copyfile(f"data/{fp}", f"sapply/{fp}")
            # count += 1
            print(f"{count} images processed\n{ignored} images discarded")
            diff[diff < 20] = 0
            diff[diff >= 20] = 1
            aggregate_data += diff
        else:
            ignored += 1
    except UnidentifiedImageError:
        print(f"Image {fp} error")

df = pd.DataFrame(aggregate_data)
df.to_csv("sapply.csv")
# display(aggregate_data)
sns.heatmap(aggregate_data)
plt.show()


