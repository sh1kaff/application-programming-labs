import argparse

from dataframe import init_df, filter_df, show_s_dist

def _parse_arguments() -> list:
    """
    Function for get arguments from cli.
    Returns:
    list: List of arguments.
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Programm gets path to csv file and output some stats information.",
        epilog="o:" 
    )
    parser.add_argument("csv", type=str, help="Path to csv")

    return parser.parse_args()

def main():
    args = _parse_arguments()

    try:
        df = init_df(args.csv)
    except Exception as e:
        print(f"Some error: {e.text}")
        exit()

    print(
        "DataFrame:\n",    
        df,
        "\n"
    )

    print(
        "Statistic information for H, W, CH:\n",
        df.loc[:, ("H", "W", "CH")].describe(),
        "\n"    
    )

    print(
        "Filter Function demonstration:\n",
        filter_df(df, 800, 1000),
        "\n"
    )

    print(
        "Sorting datafram by S column:\n",
        df.sort_values(by="S"),
        "\n"
    )

    show_s_dist(df)


if __name__ == "__main__":
    main()