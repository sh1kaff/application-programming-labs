import pandas as pd
from matplotlib import pyplot as plt
from cv2 import imread

def init_df(filename):
    LABELS = ("RP", "AP", "H", "W", "CH", "S")
    
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

def show_s_dist(df):
    df.hist(column="S")

    plt.xlabel("Pixels")
    plt.ylabel("Count")
    plt.title("Distribution Graph")
    plt.show()
