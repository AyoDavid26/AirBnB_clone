#!/usr/biin/python3
"""To define the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representing User

    where:
        email (str): email of the user
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
