from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character.
Each character is defined by a name and a status
"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initiates a Character instance.

Args:
    first_name (str) : the Character's first name
    is_alive (bool, optional): Whether the character is alive. Defaults to True
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character as dead passing is_alive from True to False."""
        if self.is_alive is True:
            self.is_alive = False


class Stark(Character):
    """A class representing a Stark.
Inherits from the Character class.
"""
    def __init__(self, first_name, is_alive=True):
        """Initiates a Stark instance.

Args:
    first_name (str): The first name of the Stark character.
    is_alive (bool, optional): Whether the Stark is alive. Defaults to True.
"""
        super().__init__(first_name, is_alive)
