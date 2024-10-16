import pandas as pd

def main():
    df = pd.read_csv("data.csv", names=list("sdfgh"))
    print(df)

if __name__ == "__main__":
    main()