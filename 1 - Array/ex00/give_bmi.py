import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert isinstance(height, list), "arguments must be lists of integers or floats"

        assert isinstance(weight, list), "arguments must be lists of integers or floats"

        assert len(height) == len(weight), "lists must be the same size"

	    assert all(
        isinstance(item, (int, float)) and item != 0 for item in height
    ), "the arguments must be of type int or float and != 0"

 	    assert all(
        isinstance(item, (int, float)) for item in weight
    ), "the arguments must be of type int or float"

		height_array = np.array(height)
		weight_array = np.array(weight)

        bmi_list = []
        for i in range(height):
            bmi_list.append(weight[i]/(height[i]**2))
        
        return bmi_list


    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")




height = [4, 4, 4]
weight = [4, 4, 4]


give_bmi(height, weight)
# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here