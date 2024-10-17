import pandas as pd
from cv2 import imread

LABELS = ("RP", "AP", "H", "W", "CH", "S")

def init_df(filename):
    df = pd.read_csv(filename, names=list(LABELS), skiprows=1)

    for idx in range( len(df) ):
        path = df.at[idx, "AP"]
        img = imread(path)
        sizes = None

        if img is not None:
            sizes = img.shape + (img.shape[0] * img.shape[1], )

        df.loc[idx, LABELS[2:]] = sizes
    
    return df


def filter_df(df, max_height, max_weight):
    return df[(df.H <= max_height) & (df.W <= max_weight)]

def main():
    df = init_df("putin.csv")

    print(df)

    print(df.loc[:, ("H", "W", "CH")].describe())

    print(filter_df(df, 800, 1000))

if __name__ == "__main__":
    main()