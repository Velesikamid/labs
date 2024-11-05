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
        raise Exception("Error: Input file not found.")

    return args


def main() -> None:
    """
    Perform image processing operations based on command-line arguments.
    """
    try:
        args = parse_arguments()
        input_path, output_path = args.input_path, args.output_path

        image = image_processor.load_image(input_path)
        if image is not None:
            image_processor.display_image_info(image)
            image_processor.plot_histogram(image)
            gray_image = image_processor.convert_to_grayscale(image)
            image_processor.save_grayscale_image(gray_image, output_path)
            image_processor.display_images(image, gray_image)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()   
