#!/usr/bin/python3
"""
This module defines a class to handle the file storage for hbnb clone
"""
import json
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
from models.city import City

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}

class FileStorage:
    """file storage class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models that are presently stored"""
        if not cls:
            return FileStorage.__objects
        elif isinstance(cls, str):
            return {key: value for key, value in FileStorage.__objects.items()
                    if value.__class__.__name__ == cls}
        else:
            return {key: value for key, value in FileStorage.__objects.items()
                    if value.__class__ == cls}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file specified by the file path"""
        json_objects = {}
        """json_objects is a dictionary"""
        for key in FileStorage.__objects:
            json_objects[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_data = json.load(f)
            for key, value in json_data.items():
                cls_name = value['__class__']
                FileStorage.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete objects from __objects if it’s present"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            del FileStorage.__objects[key]
            self.save()

    def close(self):
        """Deserialize JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Retrieve an object"""
        if isinstance(cls, str) and isinstance(id, str) and cls in classes:
            key = f"{cls}.{id}"
            obj = FileStorage.__objects.get(key, None)
            return obj
        else:
            return None

    def count(self, cls=None):
        """Count number of objects in storage"""
        total = 0
        if isinstance(cls, str) and cls in classes:
            total = len(self.all(cls))
        elif cls is None:
            total = len(FileStorage.__objects)
        return total

