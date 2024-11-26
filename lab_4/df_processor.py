import cv2
import matplotlib.pyplot as plt
import pandas as pd

def make_df(annotation_file: str) -> pd.DataFrame:
    """
    Reads the annotation file and creates a DataFrame.

    :param annotation_file: Path to the annotation file.
    :return: DataFrame containing image paths.
    :raises Exception: If the annotation file cannot be read.
    """
    try:
        df = pd.read_csv(annotation_file)
        df.columns(["absolute_path", "relative_path"])
    except Exception:
        raise Exception("The annotation could not be read!")

    return df


def add_image_dimensions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds columns for image dimensions (height, width, depth) to the DataFrame.

    :param df: DataFrame containing image paths.
    :return: Updated DataFrame with height, width, and depth columns.
    :raises Exception: If images cannot be opened
                       or their dimensions determined.
    """
    heights, widths, depths = [], [], []
    try:
        for path in df["absolute_path"]:
            img = cv2.imread(path)
            if img is not None:
                heights.append(img.shape[0])
                widths.append(img.shape[1])
                depths.append(img.shape[2])
            else:
                heights.append(None)
                widths.append(None)
                depths.append(None)
    except Exception:
        raise Exception("The images have not been opened!"
                        " It is impossible to determine"
                        " their characteristics!")
    df["height"] = heights
    df["width"] = widths
    df["depth"] = depths

    return df


def calculate_statistics(df: pd.DataFrame) -> None:
    """
    Calculates statistical information for image dimensions.

    :param df: DataFrame containing image dimensions.
    :return: Statistical summary of the height, width, and depth columns.
    :raises Exception: If statistical data cannot be calculated.
    """
    try:
        return df[["height", "width", "depth"]].describe()
    except Exception:
        raise Exception("It is impossible to calculate statistical data!")


def filter(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Filters the DataFrame to include only images within specified size limits.

    :param df: DataFrame containing image dimensions.
    :param max_height: Maximum allowed image height.
    :param max_width: Maximum allowed image width.
    :return: Filtered DataFrame.
    :raises Exception: If the DataFrame cannot be filtered.
    """
    try:
        return df[(df["height"] <= max_height) & (df["width"] <= max_width)]
    except Exception:
        raise Exception("It is impossible to filter DataFrame!")


def add_image_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a new column 'Area' to the DataFrame, representing the image area.

    :param df: DataFrame containing image dimensions.
    :return: Updated DataFrame with the 'Area' column.
    :raises Exception: If the DataFrame does not exist
                       or the column cannot be added.
    """
    try:
        df["area"] = df["height"] * df["width"]
    except Exception:
        raise Exception("It is impossible to add a new column!"
                        " Perhaps the DataFrame does not exist!")

    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the DataFrame in ascending order by the 'Area' column.

    :param df: DataFrame containing the 'Area' column.
    :return: Sorted DataFrame.
    :raises Exception: If the DataFrame cannot be sorted.
    """
    try:
        return df.sort_values(["area"], ascending=True)
    except Exception:
        raise Exception("The DataFrame cannot be sorted!"
                        " Perhaps the DataFrame does not exist!")


def plot_histogram(df: pd.DataFrame) -> None:
    """
    Plots a histogram of image areas.

    :param df: DataFrame containing the 'Area' column.
    :return: None
    :raises Exception: If the histogram cannot be displayed.
    """
    try:
        df["area"].plot(kind="hist",
                        ylabel="Frequency",
                        xlabel="Area (pixels)",
                        title="Distribution of image areas",
                        grid=True
                        )
        plt.show()
    except Exception:
        raise Exception("The histogram cannot be displayed!"
                        " Perhaps the DataFrame does not exist!")