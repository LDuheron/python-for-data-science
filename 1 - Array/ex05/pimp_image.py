import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageChops


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    try:
        assert isinstance(array, np.ndarray), "Arg must be np.ndarray"

        copy = array.copy()
        img = Image.fromarray(copy)
        inverted_image = ImageChops.invert(img)

        plt.imshow(inverted_image)
        plt.show()

        image_as_array = np.array(inverted_image)
        return image_as_array

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def ft_red(array: np.ndarray) -> np.ndarray:
    """Apply a red filter on the image received."""
    try:
        assert isinstance(array, np.ndarray), "Arg must be np.ndarray"
        copy = array.copy()

        copy[:, :, 1] = 0
        copy[:, :, 2] = 0

        img = Image.fromarray(copy)
        plt.imshow(img)
        plt.show()
        return copy

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def ft_green(array: np.ndarray) -> np.ndarray:
    """Apply a green filter on the image received."""
    try:
        assert isinstance(array, np.ndarray), "Arg must be np.ndarray"
        copy = array.copy()

        copy[:, :, 0] = 0
        copy[:, :, 2] = 0

        img = Image.fromarray(copy)
        plt.imshow(img)
        plt.show()
        return copy

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Apply a blue filter on the image received."""
    try:
        assert isinstance(array, np.ndarray), "Arg must be np.ndarray"
        copy = array.copy()

        copy[:, :, 0] = 0
        copy[:, :, 1] = 0

        img = Image.fromarray(copy)
        plt.imshow(img)
        plt.show()
        return copy

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Apply a grey filter on the image received."""
    try:
        assert isinstance(array, np.ndarray), "Arg must be np.ndarray"

        copy = array.copy()
        grey_array = copy[:, :, 1]

        img = Image.fromarray(grey_array)
        plt.imshow(img, cmap='gray')
        plt.show()
        return grey_array

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")
