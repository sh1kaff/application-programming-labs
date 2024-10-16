import pandas as pd
from cv2 import imread

def main():
    df = pd.read_csv("putin.csv", names=["RP", "AP", "H", "W", "CH"], skiprows=1)
    
    # for row in df:
    #     print(row)
    #     break

    # print(df)

    

    # print(df)

    for idx in range( len(df) ):
        path = df.at[idx, "AP"]
        img = imread(path)
        sizes = None

        if img is not None:
            sizes = img.shape

        df.iloc[idx, 2:] = sizes

        # print(sizes)


    print(df)

    # print(df.at[0, "RP"])

if __name__ == "__main__":
    main()