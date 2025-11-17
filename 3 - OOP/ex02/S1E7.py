from S1E9 import Character


class Baratheon(Character):
    """A class representing a Baratheon.

Inherits from the Character class.
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
        self.family_name = self.__class__.__name__
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """A class representing a Lannister.

Inherits from the Character class.
"""
    def __init__(self, first_name, is_alive=True):
        """Initiates a Lannister instance.

The constructor inherits attributes from the Character class and sets
Lannister-specific traits such as blue eyes and light hair.

Args:
    first_name (str): The first name of the Lannister character.
    is_alive (bool, optional): Whether the Lannister is alive.
                               Defaults to True.
"""
        super().__init__(first_name, is_alive)
        self.family_name = self.__class__.__name__
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()
