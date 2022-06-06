#!/usr/bin/python3
"""base of the pro"""

import json


class Base():
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """comment for init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str(json.dumps(list_dictionaries))
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string"""
        filename = f"{cls.__name__}.json"
        lista = []

        if list_objs is not None:
            for element in list_objs:
                lista = lista + [element.to_dictionary()]
        else:
            json_list = Base.to_json_string(empty_list)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """from json"""
        if json_string is None or len(json_string) == 0:
            json_string = []
            return json.loads(json_string)
        else:
            d = json.loads(json_string)
            return d

    @classmethod
    def create(cls, **dictionary):
        """create a new instance of Square or Rectangle"""
        instance_dady = cls.__name__

        if instance_dady == "Square":
            dummy = cls(2)

        if instance_dady == "Rectangle":
            dummy = cls(2, 2)
        
        dummy.update(**dictionary)

        return dummy
