class calculator:
    """A class representing a calculator able to do
calculations of 2 vectors."""

    def __init__(self):
        """Initiates a calculator instance."""
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiply two vectors and print the resulting vector.

    Args:
        V1 (list[float]): The first input vector.
        V2 (list[float]): The second input vector."""
        dot = 0

        for elem_v1, elem_v2 in zip(V1, V2):
            dot += (elem_v1 * elem_v2)
        print(f"Dot product is: {dot}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors and print the resulting vector.

    Args:
        V1 (list[float]): The first input vector.
        V2 (list[float]): The second input vector."""
        new_vector = []

        for elem_v1, elem_v2 in zip(V1, V2):
            new_vector.append(float(elem_v1 + elem_v2))
        print(f"Add Vector is: {new_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract two vectors and print the resulting vector.

    Args:
        V1 (list[float]): The first input vector.
        V2 (list[float]): The second input vector."""
        new_vector = []

        for elem_v1, elem_v2 in zip(V1, V2):
            new_vector.append(float(elem_v1 - elem_v2))
        print(f"Sous Vector is: {new_vector}")
