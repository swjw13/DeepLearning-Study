# 임계점 적용 -> 임계값을 기준으로 흑 / 백 을 적용해 주는 방법
import cv2
import numpy as np

image = cv2.imread("bonobono2.jpeg", cv2.IMREAD_GRAYSCALE)

images = []
ret, thres1 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY)

# THRESH_BINARY: 임계값을 넘는 거는 255, 안넘는 거는 0으로 변환

cv2.imshow("image",thres1)
cv2.waitKey()

# 적응 입계점 처리
# 사진의 부분마다 임계점 처리 방법을 다르게 적용

thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21,3)
cv2.imshow("image",thres2)
cv2.waitKey()