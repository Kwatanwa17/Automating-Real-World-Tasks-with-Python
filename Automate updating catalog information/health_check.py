#!/usr/bin/env python3

import os
import psutil
import shutil
import socket
import emails


def main():
    # Report an error if CPU usage is over 80%
    cpu_usage_alert = psutil.cpu_percent() > 80

    # Report an error if available disk space is lower than 20%
    available_disk = psutil.disk_usage('/')
    available_disk_alert = available_disk.percent > 80

    # Report an error if available memory is less than 500MB
    available_memory_alert = psutil.virtual_memory().available < 500 * 1024 * 1024

    # Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
    try:
        if socket.gethostbyname('localhost') == "127.0.0.1":
            localhost_alert = False
        else:
            localhost_alert = True
    except socket.error:
        localhost_alert = True

    # create a subjects dictionary
    subjects = {
        "Error - CPU usage is over 80%": cpu_usage_alert,
        "Error - Available disk space is less than 20%": available_disk_alert,
        "Error - Available memory is less than 500MB": available_memory_alert,
        "Error - localhost cannot be resolved to 127.0.0.1": localhost_alert,
    }

    # detect errors
    for subject, error in subjects.items():
        # send an email if there is an error
        if error:
            # send an error report
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            body = "Please check your system and resolve the issue as soon as possible."

            message = emails.generate(sender, receiver, subject, body)
            emails.send(message)


if __name__ == "__main__":
    main()
