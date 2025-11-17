class calculator:
    """A class representing a calculator able to do calculations."""

    def __init__(self, vector):
        """Initiates a calculator instance.
Args:
    vector : A vector of scalar."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector.
The method modifies the vector in place and prints the result.

Args: The scalar value to add to each element of the vector"""
        new_vector = []
        for i in self.vector:
            new_vector.append(i + object)
        self.vector = new_vector
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply a scalar to each element of the vector.
The method modifies the vector in place and prints the result.

Args: The scalar value to multiply to each element of the vector"""
        new_vector = []
        for i in self.vector:
            new_vector.append(i * object)
        self.vector = new_vector
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substract a scalar to each element of the vector.
The method modifies the vector in place and prints the result.

Args: The scalar value to substract to each element of the vector"""
        new_vector = []
        for i in self.vector:
            new_vector.append(i - object)
        self.vector = new_vector
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide a scalar to each element of the vector.
The method modifies the vector in place and prints the result.
Handles the ZeroDivision error.

Args: The scalar value to divide to each element of the vector"""
        try:
            new_vector = []
            for i in self.vector:
                new_vector.append(i / object)
            self.vector = new_vector
            print(self.vector)

        except Exception as error:
            print(f"Error: {error}")

        except ZeroDivisionError as error:
            print(f"ZeroDivisionError: {error}")
