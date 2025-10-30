import numpy as np
from PIL import Image

def ft_load(path: str):
    """Loads an image, prints its format and its pixels content in RGB format.
Args:
    Path (str): path of the image to load

Returns:
    
"""
    try:
        assert isinstance(path, str), "Arg must be of type str"
        img = Image.open(path)
    
        print(f"The shape of image is: {img.size}")

        if img.mode != "RBG":
            img = img.convert("RGB")
       
    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")
