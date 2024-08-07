#!/usr/bin/python3
"""Module defines Class `Base`"""

import csv
import json
from typing import Dict, List


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: List[Dict]):
        """Returns JSON string of passed argument"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON to file"""
        list_dicts = None
        if list_objs:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of dictionaries from argument"""
        return [] if json_string is None else json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance represented by dictionary"""
        dummy = None
        try:
            dummy = cls(width=1, height=1)
        except Exception:
            dummy = cls(size=1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return  list of instances read from file"""
        lt = []
        try:
            string = ""
            with open(f"{cls.__name__}.json", "r") as file:
                string = file.read()
            lt = [cls.create(**d) for d in cls.from_json_string(string)]
        except FileNotFoundError:
            pass
        return lt

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to a csv file"""
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            fieldnames = list_dicts[0].keys()

            with open(f"{cls.__name__}.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """Retrieves from csv file"""
        lt = []

        try:
            with open(f"{cls.__name__}.csv", "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    for k, v in row.items():
                        row[k] = int(v)
                    lt.append(cls.create(**dict(row)))
        except FileNotFoundError:
            pass

        return lt
