import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Prints the shape of given 2D array and returns a truncated
version of the array based on the provided start and end arguments.

Args:
    family (list): a list representing a 2D array
    start (int): starting point of truncated version of the array
    end (int): ending point of truncated version of ther array

Returns:
    list: truncated version of the array
"""
    try:
        assert isinstance(family, list) and isinstance(start, int) and isinstance(end, int), "expected args <list, int, int>"

        # assert all(
        #     isinstance(item, (int, float)) for item in family
        #     ), "elements of the list must be integers or floats"

        array_family = np.array(family)
        print(f"My shape is : {array_family.shape}")

        truncated_family = family[start:end]
        print(f"My new shape is : {truncated_family.shape}")

        return truncated_family

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


# print(slice_me.__doc__)
