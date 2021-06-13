import os
from PIL import Image


if __name__ == "__main__":

    src_dir = ""
    out_dir = ""

    os.makedirs(out_dir, exist_ok=True)
    for filename in os.listdir(src_dir):
        try:
            filepath = os.path.join(src_dir, filename)
            im = Image.open(filepath)
            width, height = im.size
            left = width / 10
            top = height / 7
            right = 9.25 * width / 10
            bottom = 6 * height / 7
            out_im = im.crop((left, top, right, bottom))
            out_im.save(os.path.join(out_dir, filename))
        except Exception as e:
            print("some error in ", filename)
            print("error ", e)
