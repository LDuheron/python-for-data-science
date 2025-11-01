import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """Loads an image, prints its format and its pixels content in RGB format.
Args:
    path (str): path of the image to load.

Returns:
    list: list of given image pixels content in RGB format.
"""
    try:
        assert isinstance(path, str), "Arg must be of type str"
        img = Image.open(path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        image_as_array = np.array(img)

        print(f"The shape of image is: {np.shape(image_as_array)}")

        return image_as_array

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")
