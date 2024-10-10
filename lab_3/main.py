import argparse
import cv2

from image import overlay_images, show_hist

# Добавить try
# Мб чуть красивее _parse_arguments
# test

def _parse_arguments() -> list:
    """
    Function for get arguments from cli.

    Returns:
    list: List of arguments.
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Programm gets 2 image files from stdout and transparency and adds these images using transparency.",
        epilog="o:" 
    )
    parser.add_argument("img_main", type=str, help="Main image.")
    parser.add_argument("img_overlay", type=str, help="Overlay image.")
    parser.add_argument("trn", type=int, help="TRaNsparency: value from 0 to 100.")
    parser.add_argument("-f", "--force", action="store_true", help="Force using resize \
                         overlay image if it size not match with main image.")
    
    return parser.parse_args()

def display(img, frameName="OpenCV Image"):
    h, w = img.shape[0:2]
    neww = 800
    newh = int(neww*(h/w))
    img = cv2.resize(img, (neww, newh))
    cv2.imshow(frameName, img)
    cv2.waitKey(0)

def main() -> None:
    args = _parse_arguments()
    
    img_main = cv2.imread(args.img_main)
    img_overlay = cv2.imread(args.img_overlay)

    for img, img_name in zip( (img_main, img_overlay), (args.img_main, args.img_overlay) ):
        print(f"{img_name} sizes: {img.shape}, {img.size}b")
        show_hist(img, img_name)

    result = overlay_images(img_main, img_overlay, args.trn, force=args.force)

    # cv2.imshow("Overlay", result)
    display(result, "ovrlay")
    cv2.waitKey(0)


if __name__ == "__main__":
    main()

