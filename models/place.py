#!/usr/bin/python3
"""To define the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representing a place

    where:
        city_id (str): City id
        user_id (str): User id
        name (str): Name of the palce
        description (str): Description of the place
        number_rooms (int): Total number of rooms in the place
        number_bathrooms (int): Total number of bathroom
        max_guest (int): Maximum number of guests in the place
        price_by_night (int): Price of the place by night
        latitude (float): The latitude of the place
        longitude (float): Longitude of the place
        amenity_ids (list): List of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
