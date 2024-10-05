#!/usr/bin/python3
"""Defines a JSON string conversion function."""

import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.
    
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
