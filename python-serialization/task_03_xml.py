#!/usr/bin/python3
"""Module task_03_xml"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function that serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the fike to save the XML data to.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Function that deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Return:
        dictionnary (dict): The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionnary = {}
    for child in root:
        dictionnary[child.tag] = child.text
    return dictionnary
