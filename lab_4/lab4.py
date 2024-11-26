import argparse
import os

import df_processor


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments to retrieve the path to the annotation file.

    :return: Parsed arguments containing the annotation file path.
    :raises Exception: If the annotation file does not exist.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation_path",
                        type=str,
                        help="Path to the annotation"
                        )

    args = parser.parse_args()

    if not os.path.exists(args.annotation_path):
        raise Exception("The annotation file was not found!")

    return args


def main() -> None:
    """
    Main execution function for processing the annotation file.

    Workflow:
        - Parses command-line arguments to get the annotation file path.
        - Reads the annotation file into a DataFrame.
        - Adds image dimensions and calculates statistics.
        - Filters images by size limits.
        - Computes and sorts image areas.
        - Plots a histogram of image areas.

    :return: None
    :raises Exception: If any step in the workflow fails.
    """
    try:
        args = parse_arguments()
        annotation_file = args.annotation_path

        df = df_processor.make_df(annotation_file)
        print(df)

        df = df_processor.add_image_dimensions(df)

        print("Statistical information:")
        print(df_processor.calculate_statistics(df), end="\n\n")

        max_height, max_width = 500, 500
        filtered_df = df_processor.filter(df, max_height, max_width)
        print("Filtered data:")
        print(filtered_df, end="\n\n")

        df = df_processor.add_image_area(df)
        df = df_processor.sort_by_area(df)
        print("Sorted data:")
        print(df, end="\n\n")

        df_processor.plot_histogram(df)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
