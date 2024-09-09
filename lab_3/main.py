# https://habr.com/ru/companies/otus/articles/558426/
# https://tproger.ru/translations/opencv-python-guide

import cv2
from matplotlib import pyplot as plt


def main():
    img = cv2.imread("images/1.jpg")
    print(img.shape)  # sizes in h,w,c
    print(img.size)  # size in bytes

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



if __name__ == "__main__":
    main()

