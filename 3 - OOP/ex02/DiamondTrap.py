from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing a Baratheon.

Inherits from class Baratheon and Lannister.
"""
    def __init__(self, first_name, is_alive=True):
        """Initiates a Baratheon instance.

The constructor inherits attributes from the Character class and sets
Baratheon-specific traits such as brown eyes and dark hair.

Args:
    first_name (str): The first name of the Baratheon character.
    is_alive (bool, optional): Whether the Baratheon is alive.
                               Defaults to True.
"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes: str):
        """Set the eye description for the object.
Args:
    new_eyes (str) : The new value describing the object's eyes."""
        self.eyes = new_eyes

    def get_eyes(self) -> str:
        """Retrieve the current eye description.

Returns:
str : The value describing the object's eyes."""
        return self.eyes

    def set_hairs(self, new_hairs: str):
        """Set the hair description for the object.
Args:
    new_hairs (str) : The new value describing the object's hairs."""
        self.hairs = new_hairs

    def get_hairs(self) -> str:
        """Retrieve the current hair description.

Returns:
str : The value describing the object's hairs."""
        return self.hairs
