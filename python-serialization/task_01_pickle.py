#!/usr/bin/python3
"""Module task_01_pickle"""
import pickle


class CustomObject:
    """
    Custom object class with attributes

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Wether the person is a student.
    """
    def __init__(self, name, age, is_student):
        """Instantiation of CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Method that prints the attributes of the object in formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Method that serializes the object and saves it to a file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Method class that deserializes an object from a file,
        And returns an instance of CustomObject.

        Args:
            filename (str): The name of the file,
                To load the serialized object from.

        Return:
            CustomObject:
                An instance of CustomObject if deserialization is succesful,
                Otherwise None.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            return None
