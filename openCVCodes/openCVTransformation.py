import cv2 as c
import numpy as np

image = c.imread("bonobono3.png")

# 이미지의 크기를 바꾸는 방법
expand = c.resize(image, None, fx = 0.5, fy = 0.5, interpolation = c.INTER_CUBIC)
c.imshow("image",expand)
c.waitKey(0)

# 이미지의 위치를 바꾸는 방법
# 변환행렬을 사용한다
height, width = image.shape[:2]
M = np.float32([[1,0,50],[0,1,10]])
dst = c.warpAffine(image, M, (width, height))
c.imshow("image", dst)
c.waitKey(0)

# 이미지를 회전하는 방법
M = c.getRotationMatrix2D((width/2, height / 2), 90, 0.5)
dst = c.warpAffine(image, M, (width, height))
c.imshow("image", dst)
c.waitKey(0)