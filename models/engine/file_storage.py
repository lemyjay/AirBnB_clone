#!/usr/bin/python3
"""
module that defines the FileStorage class
"""
import json
from datetime import datetime



class FileStorage:
    """
    The FileStorage class serializes instances to a JSON
    file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized objects.

    Methods:
        all(self): Returns the dictionary __objects.
        new(self, obj): Sets in __objects the obj with key <obj class name>.id.
        save(self): Serializes __objects to the JSON file (path: __file_path).
        reload(self): Deserializes the JSON file to __objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in  __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, _ = key.split('.')
                    module = __import__('models', fromlist=[class_name])
                    class_type = getattr(module, class_name)
                    print(f"here is the class type {class_type}")
                    if class_type:
                        obj_data['created_at'] = datetime.strptime(
                            obj_data['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
                        obj_data['updated_at'] = datetime.strptime(
                            obj_data['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
                        obj = class_type(**obj_data)
                        # Directly update __objects dictionary
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
