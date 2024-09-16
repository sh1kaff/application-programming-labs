import cv2
from numpy import ndarray

def get_hist(img: ndarray, channel: int) -> ndarray:
    """
    Returns hist for image for specify channel.

    Parameters:
    img (ndarry): Input image.
    channel (ing): One channel of 0, 1, 2.

    Returns:
    ndarray: Output hist.
    """
    
    if channel > 2 or channel < 0:
        raise ValueError("Argument channel must be between 0 and 2 (includes)!")

    return cv2.calcHist([img], [channel], None, [256], [0, 256])

def overlay_images(img_main: ndarray, img_overlay: ndarray, trn: int, force: bool = True) -> ndarray:
    """
    Overlay 2 images.

    Parameters:
    img_main (ndarray): Main image.
    img_overlay (ndarray): Overlay image.
    trn (ing): Transparency value in percentage between 0 and 100.
    force (bool): Force resize img_overlay if it size don't match.

    Returns:
    ndarray: Result added image.
    """
    if trn > 100 or trn < 0:
        raise ValueError("Percentage must be between 0 and 100!")

    trn_result = 1 - trn / 100

    if not force and (img_main.shape[:2] != img_overlay.shape[:2]):
        raise ValueError(f"Sizes don't match: {img_main.shape[:2]} and {img_overlay.shape[:2]}")
    elif force:
        img_overlay = cv2.resize(img_overlay, (img_main.shape[1], img_main.shape[0]))
        
    img_result = cv2.addWeighted(img_main, 1 - trn_result, img_overlay, trn_result, 0)

    return img_result
