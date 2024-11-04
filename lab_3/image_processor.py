import cv2
import matplotlib.pyplot as plt


class ImageProcessor:
    def __init__(self, input_path: str, output_path: str) -> None:
        """
        Initialize the ImageProcessor with input and output paths.

        :param input_path: Path to the input image.
        :param output_path: Path to save the grayscale image.
        """
        self.input_path = input_path
        self.output_path = output_path
        self.image = None
        self.gray_image = None

    def load_image(self) -> bool:
        """
        Load the image from the specified input path.

        :raises FileNotFoundError: If the image file cannot be found.
        :return: True if the image is loaded successfully, otherwise False.
        """
        try:
            self.image = cv2.imread(self.input_path)
            if self.image is None:
                raise FileNotFoundError("Error: Failed to load the image."
                                        " Please check the file path and try"
                                        " again.")
        except FileNotFoundError as e:
            print(e)
            return False
        except Exception as e:
            print("An unexpected error occurred while loading the image:", e)
            return False
        return True

    def display_image_info(self) -> None:
        """
        Display the image size and number of channels.
        """
        if self.image is not None:
            height, width, channels = self.image.shape
            print(f"Image size: {width}x{height}, channels: {channels}.")

    def plot_histogram(self) -> None:
        """
        Plot the histogram of the image for each color channel.
        """
        if self.image is None:
            print("Error: No image loaded to plot histogram.")
            return
        colors = ('b', 'g', 'r')
        plt.figure()
        plt.title("Image Histogram")
        plt.xlabel("Intensity")
        plt.ylabel("Pixel count")
        for i, color in enumerate(colors):
            hist = cv2.calcHist([self.image], [i], None, [256], [0, 256])
            plt.plot(hist, color=color)
            plt.xlim([0, 256])
        plt.show()

    def convert_to_grayscale(self) -> None:
        """
        Convert the loaded image to grayscale and store it in gray_image.
        """
        if self.image is None:
            print("Error: No image loaded to convert to grayscale.")
            return
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def save_grayscale_image(self) -> None:
        """
        Save the grayscale image to the specified output path.

        :raises Exception: If an error occurs while saving the image.
        """
        if self.gray_image is None:
            print("Error: No grayscale image to save.")
            return
        try:
            cv2.imwrite(self.output_path, self.gray_image)
            print(f"Grayscale image saved at {self.output_path}")
        except Exception as e:
            print("An error occurred while saving the grayscale image:", e)

    def display_images(self) -> None:
        """
        Display the original and grayscale images side by side.
        """
        if self.image is None or self.gray_image is None:
            print("Error: Images not ready for display.")
            return
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.title("Original Image")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(self.gray_image, cmap='gray')
        plt.title("Grayscale Image")
        plt.axis('off')

        plt.show()
