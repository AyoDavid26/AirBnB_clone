#!/usr/bin/python3
"""To define the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representing the review class

    where:
        place_id (str): The place id
        user_id (str): The user id
        text (str): The review text
    """

    place_id = ""
    user_id = ""
    text = ""
