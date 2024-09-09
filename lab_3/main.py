# https://habr.com/ru/companies/otus/articles/558426/
# https://tproger.ru/translations/opencv-python-guide
# https://ru.wikipedia.org/wiki/Гистограмма_(фотография)
# https://www.geeksforgeeks.org/python-opencv-cv2-calchist-method/
# https://docs.opencv.org/3.4/d8/dbc/tutorial_histogram_calculation.html

import argparse

import cv2
from matplotlib import pyplot as plt

def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="...",
        epilog="o:" 
    )
    parser.add_argument("img_main", type=str, help="...")
    parser.add_argument("img_overlay", type=str, help="....")
    
    return parser.parse_args()

def show_hist(img):
    colors = ("blue", "green", "red", "black")
    legend = (*map(lambda s: s.capitalize() + " channel", colors[:-1]), "Summary")

    hist = None
    for channel, color in zip( (0, 1, 2), colors[:-1] ):
        current_hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
        if hist is None:
            hist = current_hist
        else:
            hist += current_hist
        plt.plot(current_hist, color=color)

    plt.plot(hist, color=colors[-1])
    plt.ylabel("Pixels")
    plt.xlabel("Brightness")

    plt.legend(legend)

    plt.title("Image Histogram")
    plt.show()


def main():
    args = _parse_arguments()
    
    img1 = cv2.imread(args.img_main)
    img2 = cv2.imread(args.img_overlay)

    print(img1.shape)  # sizes in h,w,c
    print(img1.size)  # size in bytes

    show_hist(img1)
    show_hist(img2)

    



if __name__ == "__main__":
    main()

