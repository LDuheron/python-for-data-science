from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character.
Each character is defined by a name and a status"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initiates a Character instance.

Args:
    first_name (str) : the Character's first name
    is_alive (bool, optional): Whether the character is alive. Defaults to True
"""
        self.first_name = first_name
        self.is_alive = is_alive

    def set_is_alive(self, state: bool):
        """Set the character's living status.

Args:
    state (bool): True if the character is alive, False otherwise.
"""
        self.is_alive = state


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

    def die(self):
        """Set the Stark character as dead calling the parent
class method `set_is_alive(False)`."""
        super().set_is_alive(False)
