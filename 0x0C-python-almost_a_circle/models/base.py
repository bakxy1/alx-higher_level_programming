#!/usr/bin/python3
"""Module defines Class `Base`"""

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
