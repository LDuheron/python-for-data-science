def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """Calculate BMI values given lists of height and weight.

Args:
    height (list[int | float]): A list of height values.
    weight (list[int | float]): A list of weight values.

Returns:
    list[int | float] : A list of BMI values calculate from
    the given height and weight pairs.
"""
    try:
        assert isinstance(height, list), "arguments must be lists"

        assert isinstance(weight, list), "arguments must be lists"

        assert len(height) == len(weight), "lists must be the same size"

        assert all(
            isinstance(item, (int, float)) for item in height
            ), "elements of the list must be integers or floats"

        assert all(
            isinstance(item, (int, float)) for item in weight
            ), "the arguments must be lists of elements type int or float"

        bmi = [
            elem_w/(elem_h**2)
            for elem_w, elem_h in zip(weight, height)
        ]
        return bmi

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except ZeroDivisionError as error:
        print(f"ZeroDivisionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit on BMI values and return whether each value is below it.

Args:
    bmi (list[int | float]): A list of ints and floats representing BMI values
    limit (int): The BMI threshold to compare against.

Returns:
    A list of booleans where each element is True if the corresponding
    value is below the limit, otherwise False.
"""
    assert isinstance(bmi, list), "first argument must be a list"

    assert isinstance(limit, int), "second argument must be an integer"

    assert all(
        isinstance(item, (int, float)) for item in bmi
    ), "elements of the list must be integers or floats"

    is_above_limit = []
    for elem in bmi:
        is_above_limit.append(elem > limit)
    return is_above_limit
