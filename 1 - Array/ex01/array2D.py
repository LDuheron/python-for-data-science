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
        assert isinstance(family, list), "expected args <list, int, int>"

        assert isinstance(start, int), "expected args <list, int, int>"

        assert isinstance(end, int), "expected args <list, int, int>"

        len_row = len(family[0])
        assert all(len(elem) == len_row for elem in family
                   ), "elements in the list must be the same size"

        print(f"My shape is : ({len(family)}, {len_row})")

        new_family = family[start:end]
        print(f"My new shape is : ({len(new_family)}, {len(new_family[0])})")

        return new_family

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")
