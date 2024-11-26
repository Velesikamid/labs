import argparse
import os

import numpy as np
import pandas as pd

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation_path", type=str, help="Path to the annotation")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.annotation_path):
        raise Exception("Error: The annotation file was not found.")
    
    return args

def make_df(annotation_file):
    df = pd.read_csv(annotation_file)
    
    return df

def main():
    args = parse_arguments()
    annotation_file = args.annotation_path
    df = make_df(annotation_file)
    print(df)

if __name__ == "__main__":
    main()
