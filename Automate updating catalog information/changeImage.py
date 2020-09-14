#!/usr/bin/env python3

import os
import sys
import glob
from PIL import Image


def main():
    # get necessary paths and all file names
    root = os.getcwd()
    dir_path = os.path.join(root, "supplier-data", "images")
    file_names = os.listdir(dir_path)

    for file in file_names:
        try:
            with Image.open(os.path.join(dir_path, file)) as img:
                print("Processing: " + file)
                img_rgb = img.convert("RGB")
                img_resize = img_rgb.resize((600, 400))
                img_resize.save(os.path.join(dir_path, file), "jpeg")
                img.close()
            print("Saved: " + file)
        except OSError:
            print("Skip: " + file)


if __name__ == '__main__':
    main()
