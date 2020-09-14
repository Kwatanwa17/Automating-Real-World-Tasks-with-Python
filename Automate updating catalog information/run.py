#! /usr/bin/env python3

import os
import sys
import re
import requests


def main():
    root = os.getcwd()
    input_dir = os.path.join(root, "supplier-data", "descriptions")
    txt_file_names = os.listdir(input_dir)
    ip = sys.argv[1]
    url = "http://" + ip + "/fruits/"
    print("URL: " + url)

    for file_name in txt_file_names:
        try:
            with open(os.path.join(input_dir, file_name)) as f:
                lines = f.readlines()
                lines = [line.strip() for line in lines]
                f.close()
                keys = ["name", "weight", "description"]
                data = dict(zip(keys, lines))
                # remove lb unit and convert it as integer
                obj = re.search(r'[1-9]+', data["weight"])
                data["weight"] = int(obj.group())
                # add image_name field
                data["image_name"] = file_name.replace("txt", "jpeg")
                print(data)

            # post requests
            r = requests.post(url, json=data)
            print(r.status_code)

        except IOError:
            print("IOError: " + file_name)


if __name__ == '__main__':
    main()
