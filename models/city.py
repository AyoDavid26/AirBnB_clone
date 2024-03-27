#!/usr/bin/python3
"""Defining the class City"""
from model.base_model import BaseModel


class City(BaseModel):
    """Representing a city

    where:
        state_id (str): The state id
        name (str): Name of the city
    """

    state_id = ""
    name = ""
