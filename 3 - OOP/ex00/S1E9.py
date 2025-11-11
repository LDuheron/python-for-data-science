from abc import ABC, abstractmethod


class Character(ABC):
    """A class representing a character which is defined
by a name and a status"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initiates the Character class

Args:
    self: class convention
    first_name (string) : name of the Character
    is_alive (bool) : status of the Character,
                            set at True by default
        """
        self.first_name = first_name
        self.is_alive = is_alive

    # @abstractmethod
    def set_is_alive(self, state: bool):
        """Set the is_alive_value to the given bool value"""
        self.is_alive = state


class Stark(Character):
    """Create a class Stark which inherits from Character class"""
    def __init__(self, first_name, is_alive=True):
        """Initiates the Stark class

Args:
    self: class convention
    first_name (string) : name of the Stark Character
    is_alive (bool) : status of the Stark Character,
                     set at True by default
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Set the is_alive value to false calling the
parent class method set_is_alive()"""
        # self.is_alive = False
        super().set_is_alive(False)
