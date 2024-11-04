import argparse
import os

import image_processor


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for input and output image paths.

    :return: Parsed arguments containing input and output paths.
    """
    parser = argparse.ArgumentParser(
        description="Image processing: size, histogram, grayscale conversion."
    )
    parser.add_argument("input_path", type=str, help="Path to the input image")
    parser.add_argument("output_path",
                        type=str,
                        help="Path to save the grayscale image"
                        )

    args = parser.parse_args()

    if not os.path.exists(args.input_path):
        print("Error: Input file not found.")
        exit(1)

    return args


def main() -> None:
    """
    Perform image processing operations based on command-line arguments.
    """
    args = parse_arguments()
    processor = image_processor.ImageProcessor(
        args.input_path,
        args.output_path
    )

    if processor.load_image():
        processor.display_image_info()
        processor.plot_histogram()
        processor.convert_to_grayscale()
        processor.save_grayscale_image()
        processor.display_images()


if __name__ == "__main__":
    main()
