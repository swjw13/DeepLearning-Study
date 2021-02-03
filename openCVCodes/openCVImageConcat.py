import cv2
import numpy as np

image1 = cv2.imread("bonobono2.jpeg")
image1.resize(400,400)
image2 = cv2.imread("bonobono3.png")
image2.resize(400,400)

result1 = cv2.add(image1, image2)
cv2.imshow("result1", result1)
cv2.waitKey()

result2 = image1 + image2
cv2.imshow("result2", result2)
cv2.waitKey()