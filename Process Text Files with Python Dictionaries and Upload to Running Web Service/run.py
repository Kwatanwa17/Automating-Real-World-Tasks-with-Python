#! /usr/bin/env python3

import os
import sys
import requests


def main():
    input_dir = "/data/feedback"
    txt_file_names = os.listdir(input_dir)
    ip = sys.argv[1]
    url = "http://" + ip + "/feedback/"
    print("URL: " + url)

    for file_name in txt_file_names:
        try:
            with open(os.path.join(input_dir, file_name)) as f:
                lines = f.readlines()
                lines = [line.strip() for line in lines]
                f.close()
                keys = ["title", "name", "date", "feedback"]
                data = dict(zip(keys, lines))
                print(data)

        # post requests
            r = requests.post(url, json=data)
            print(r.status_code)
            # if int(r.status_code) == 201:
            #     print("POST successfully: " + file_name)
        except IOError:
            print("IOError: " + file_name)


if __name__ == '__main__':
    main()
