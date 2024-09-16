import cv2

def get_hist(img, channel):
    return cv2.calcHist([img], [channel], None, [256], [0, 256])

def overlay_images(img_main, img_overlay, trn: int):
    if trn > 100 or trn < 0:
        raise ValueError("fignya")

    trn_result = 1 - trn / 100

    img_overlay_resized = cv2.resize(img_overlay, (img_main.shape[1], img_main.shape[0]))
    img_result = cv2.addWeighted(img_main, 1 - trn_result, img_overlay_resized, trn_result, 0)

    return img_result
