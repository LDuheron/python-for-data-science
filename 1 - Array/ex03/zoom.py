import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from PIL import Image


def zoom(array_input: np.ndarray) -> np.ndarray:
    """Zoom into an image, convert it to grayscale, prints informations,
show the image and return an image in 3D array format (height, width, 1).

Args:
    array_input (np.ndarray): numpy_array of the image to zoom into.

Returns:
    np.ndarray: A 3D numpy array of shape (height, width, 1) representing the
                    grayscale image.
"""
        assert isinstance(array_input, np.ndarray), "Arg must be np.ndarray"

        resized_array = array_input[100:500, 450:850]

        img = Image.fromarray(resized_array).convert('L').resize((400, 400))

        array = np.array(img)

        array_3d = array[:, :, np.newaxis]

        plt.figure(figsize=(6, 6), facecolor='white')
        plt.title("Zoomed grayscale image")
        plt.imshow(array, cmap='gray')
        plt.show()
        print(f"New shape after slicing : {array_3d.shape} or {array.shape}")

        return array_3d



def main():
    try:
        img = ft_load("animal.jpeg")
        print(img)

        zoom_img = zoom(img)
        print(zoom_img)

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
