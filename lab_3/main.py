# https://habr.com/ru/companies/otus/articles/558426/
# https://tproger.ru/translations/opencv-python-guide

import cv2
from sys import getsizeof

img = cv2.imread("images/1.jpg")
print(img.size)


print(type(img))


# cv2.imshow("cat", img)
# cv2.waitKey(0)
