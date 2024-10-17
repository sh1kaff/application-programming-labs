import pandas as pd
from cv2 import imread

LABELS = ("RP", "AP", "H", "W", "CH", "S")

def init_df(filename):
    df = pd.read_csv(filename, names=list(LABELS), skiprows=1)

    for idx in range( len(df) ):
        path = df.at[idx, "AP"]
        img = imread(path)
        sizes = None

        if img is None:
            df.drop(index=idx, inplace=True)
            continue

        sizes = img.shape + (img.shape[0] * img.shape[1], )
        df.loc[idx, LABELS[2:]] = sizes
    
    return df


def filter_df(df, max_height, max_weight):
    return df[(df.H <= max_height) & (df.W <= max_weight)]

def main():
    df = init_df("putin.csv")

    print(
        "DataFrame:\n",    
        df
    )

    print(
        "Statistic information for H, W, CH:\n",
        df.loc[:, ("H", "W", "CH")].describe()    
    )

    print(
        "Filter Function demonstration:\n",
        filter_df(df, 800, 1000)
    )

    print(
        "Sorting datafram by S column:\n",
        df.sort_values(by="S")
    )

if __name__ == "__main__":
    main()