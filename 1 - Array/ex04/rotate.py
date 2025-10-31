import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from PIL import Image


def zoom(array_input: np.ndarray) -> np.ndarray:
    """Zoom into an image, convert it to grayscale
    and return an image in 3D array format (height, width, 1).

Args:
    array_input (np.ndarray): numpy_array of the image to zoom into.

Returns:
    np.ndarray: A 3D numpy array of shape (height, width, 1) representing the
                    grayscale image.
"""
    try:
        assert isinstance(array_input, np.ndarray), "Arg must be np.ndarray"

        resized_array = array_input[100:500, 450:850]

        img = Image.fromarray(resized_array).convert('L').resize((400, 400))

        array = np.array(img)

        array_3d = array[:, :, np.newaxis]

        print(f"The shape of image is : {array_3d.shape} or {array.shape}")

        return array_3d

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def rotate(input_array: np.ndarray) -> np.ndarray:
    """Rotate an image and prints informations.

Args:
    array_input (np.ndarray): numpy_array of the image to zoom into.

Returns:
    np.ndarray: A 3D numpy array of shape (height, width) representing the
                    transposed grayscale image.
"""
    try:
        assert isinstance(input_array, np.ndarray), "Arg must be np.ndarray"

        if input_array.ndim == 3:
            squeezed_array = np.squeeze(input_array, axis=2)

        transposed_array = np.transpose(squeezed_array)
        print(f"New shape after Transpose: {transposed_array.shape}")

        img = Image.fromarray(transposed_array)
        plt.figure(figsize=(6, 6), facecolor='white')
        plt.title("Zoomed grayscale image")
        plt.imshow(img, cmap='gray')
        plt.show()

        return transposed_array

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


def main():
    try:
        img = ft_load("animal.jpeg")

        zoom_img = zoom(img)
        print(zoom_img)

        rotate_img = rotate(zoom_img)
        print(rotate_img)

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
