from matplotlib import pyplot as plt
from numpy import ndarray
from image import get_hist

def show_hist(img: ndarray) -> None:
    """
    Show hist for image 'img' using matplotlib.

    Parameters:
    img (ndarray): Input image.
    """
    colors = ("blue", "green", "red", "black")
    legend = (*map(lambda s: s.capitalize() + " channel", colors[:-1]), "Summary")

    hist = None
    for channel, color in zip( (0, 1, 2), colors[:-1] ):
        current_hist = get_hist(img, channel)
        if hist is None:
            hist = current_hist
        else:
            hist += current_hist
        plt.plot(current_hist, color=color)

    plt.plot(hist, color=colors[-1])
    plt.ylabel("Pixels count")
    plt.xlabel("Pixels range")

    plt.legend(legend)

    plt.title("Image Histogram")
    plt.show()