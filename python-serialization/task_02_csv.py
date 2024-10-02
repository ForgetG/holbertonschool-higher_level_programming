#!/usr/bin/python3
"""Module task_02_csv"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Function that converts CSV file to JSON file.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Return:
        bool: True if conversion succesful,
        False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
