import pandas as pd
from cv2 import imread

def main():
    filename = "putin.csv"
    df = pd.read_csv(filename, names=["RP", "AP", "H", "W", "CH"], skiprows=1)

    for idx in range( len(df) ):
        path = df.at[idx, "AP"]
        img = imread(path)
        sizes = None

        if img is not None:
            sizes = img.shape

        df.iloc[idx, 2:] = sizes

    print(df.iloc[:, 2:].describe())

if __name__ == "__main__":
    main()