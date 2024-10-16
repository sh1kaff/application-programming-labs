import pandas as pd
from cv2 import imread

def main():
    df = pd.read_csv("putin.csv", names=["RP", "AP", "H", "W", "CH"], skiprows=1)
    
    # for row in df:
    #     print(row)
    #     break

    for idx in range( len(df) ):
        path = df.at[idx, "AP"]
        img = imread(path)
        sizes = img.size if img else None
        print(sizes)


    print(len(df))

    # print(df.at[0, "RP"])

if __name__ == "__main__":
    main()