#!/usr/bin/env python3

import os
import sys
import glob
from PIL import Image


def main():
    # get necessary paths and all file names
    root = os.getcwd()
    input_dir = os.path.join(root, "images")
    output_dir = os.path.join(root, "opt", "icons")
    file_names = os.listdir(input_dir)

    # create output dir
    try:
        os.makedirs(output_dir)
    except FileExistsError:
        print("Directory already exists: " + "\n" + output_dir)

    for file in file_names:
        try:
            with Image.open(os.path.join(input_dir, file)) as img:
                print("Processing: " + file)
                img_rotate = img.rotate(-90).convert("RGB")
                img_resize = img_rotate.resize((128, 128))
                img_resize.save(os.path.join(output_dir, file), "jpeg")
                img.close()
            print("Saved: " + file)
        except OSError:
            print("Skip: " + file)


if __name__ == '__main__':
    main()
