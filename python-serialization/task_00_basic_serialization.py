#!/usr/bin/python3
"""Module task_00_basic_serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the data to JSON and save it to the specified file.

    Args:
        data (dict): A Python Dictionary with data.
        filename (str): The filename of the output JSON file.
            If the output file alreday exists it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified JSON file.

    Args: filename (str): The filename of the input JSON file

    Return:
        dict: A Python Dictionary with the deserialized JSON data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
