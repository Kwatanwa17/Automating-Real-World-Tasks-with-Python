#!/usr/bin/env python3

import os
from PIL import Image


def main():
    # get necessary paths and all file names
    root = os.getcwd()
    dir_path = os.path.join(root, "supplier-data", "images")
    file_names = os.listdir(dir_path)

    for file_name in file_names:
        try:
            with Image.open(os.path.join(dir_path, file_name)) as img:
                print("Processing: " + file_name)
                img_rgb = img.convert("RGB")
                img_resize = img_rgb.resize((600, 400))
                new_file_name = file_name.replace("tiff", "jpeg")
                img_resize.save(os.path.join(dir_path, new_file_name), "jpeg")
                img.close()
            print("Saved: " + new_file_name)
        except OSError:
            print("Skip: " + file_name)


if __name__ == '__main__':
    main()
