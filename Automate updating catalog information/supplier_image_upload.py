#!/usr/bin/env python3

import os
import sys
import requests


def main():
    root = os.getcwd()
    dir_path = os.path.join(root, "supplier-data", "images")
    file_names = os.listdir(dir_path)
    ip = sys.argv[1]
    url = "http://" + ip + "/upload/"
    print("URL: " + url)

    for file_name in file_names:
        if "jpeg" in file_name:
            try:
                with open(os.path.join(dir_path, file_name), "rb") as file:
                    # post requests
                    r = requests.post(url, files={'file': file})
                    file.close()
                    print(r.status_code)
            except IOError:
                print("IOError: " + file_name)


if __name__ == '__main__':
    main()
