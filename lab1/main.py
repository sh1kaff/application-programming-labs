import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Returns most count number codes",
        epilog="o:" 
    )
    parser.add_argument("filename", type=str, help="Path to file.")
    
    args = parser.parse_args()