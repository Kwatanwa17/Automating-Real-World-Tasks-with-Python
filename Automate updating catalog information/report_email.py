#!/usr/bin/env python3

import json
import locale
import sys
import os
import reports
import emails
import datetime


def process_data():
    """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    input_dir = "/supplier-data/descriptions"
    txt_file_names = os.listdir(input_dir)
    summary = []

    for file_name in txt_file_names:
        try:
            with open(os.path.join(input_dir, file_name)) as text:
                lines = text.readlines()
                lines = [line.strip() for line in lines][:2]
                keys = ["name", "weight"]
                summary.append("<br/>".join(key + ": " + "line" for key, line in zip(keys, lines)))

        except IOError:
            print("IOError: " + file_name)

    return summary


def main():
    """Process the JSON data and generate a full report out of it."""
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    summary = process_data()
    print(summary)
    filename = "processed.pdf"

    # turn this into a PDF report
    paragraph = "<p></p>".join(summary)
    reports.generate(filename, "Processed Update on" + datetime.date.today().strftime("%B %d, %Y"), paragraph)

    # send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, filename)
    emails.send(message)


if __name__ == "__main__":
    main()
