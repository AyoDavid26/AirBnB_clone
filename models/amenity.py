#!/usr/bin/python3
"""To define the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing an Amenity

    where:
        name (str): Name of the amenity
    """

    name = ""
