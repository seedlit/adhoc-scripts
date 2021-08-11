import os
from PIL import Image
import numpy as np


if __name__ == "__main__":

    dir_1 = ""
    dir_2 = ""
    dir_3 = ""

    out_dir = ""

    os.makedirs(out_dir, exist_ok=True)
    
    for img_name in os.listdir(dir_1):
        try:
            ndvi_path = os.path.join(dir_1, img_name.replace(".png", "_ndvi.png"))
            img1_path = os.path.join(dir_1, img_name)
            img2_path = os.path.join(dir_2, img_name)
            img3_path = os.path.join(dir_3, img_name)

            ndvi_array = np.asarray(Image.open(ndvi_path))
            img1_array = np.asarray(Image.open(img1_path))
            img2_array = np.asarray(Image.open(img2_path))
            img3_array = np.asarray(Image.open(img3_path))

            stacked_array = np.hstack((ndvi_array, img1_array, img2_array, img3_array))
            stacked_img = Image.fromarray(stacked_array)

            out_img_path = os.path.join(out_dir, img_name)
            stacked_img.save(out_img_path)
        
        except Exception as e:
            print("some error in ", img_name)
            print(e)
