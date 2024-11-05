import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_image(input_path: str) -> np.ndarray:
    """
    Load the image from the specified input path.

    :raises FileNotFoundError: If the image file cannot be found.
    :return: The image.
    """
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError("Error: Failed to load the image."
                                " Please check the file path and try"
                                " again.")
    return image


def display_image_info(image: np.ndarray) -> None:
    """
    Display the image size and number of channels.
    """
    if image is not None:
        height, width, channels = image.shape
        print(f"Image size: {width}x{height}, channels: {channels}.")


def make_histogram(image: np.ndarray, i: int) -> np.ndarray:
    """
    Makes the histogram of the image for one color channel.

    :param image: The image.
    :param i: Number of color channel.
    :raises Exception: If the image is not loaded.
    :return: The histogram for one color channel.
    """
    if image is None:
        raise Exception("Error: No image loaded to plot histogram.")
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    return hist


def plot_histogram(image: np.ndarray) -> None:
    """
    Plot the histogram of the image for each color channel.
    """
    colors = ('b', 'g', 'r')
    plt.figure()
    plt.title("Image Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Pixel count")
    for i, color in enumerate(colors):
        hist = make_histogram(image, i)
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert the loaded image to grayscale.

    :param image: The image.
    :raises Exception: If the image is not loaded.
    :return: Converted image.
    """
    if image is None:
        raise Exception("Error: No image loaded to convert to grayscale.")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def save_grayscale_image(gray_image: np.ndarray, output_path: str) -> None:
    """
    Save the grayscale image to the specified output path.

    :param gray_image: The grayscale image.
    :param output_path: The path to save the grayscale image.
    :raises Exception: If the grayscale image is not exist.
    """
    if gray_image is None:
        raise Exception("Error: No grayscale image to save.")
    cv2.imwrite(output_path, gray_image)


def display_images(image: np.ndarray, gray_image: np.ndarray) -> None:
    """Display the original and grayscale images side by side.

    :param image: The original image.
    :param gray_image: The grayscale image.
    :raises Exception: If one of the images is not exist.
    """
    if image is None or gray_image is None:
        raise Exception("Error: Images not ready for display.")
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    plt.show()
