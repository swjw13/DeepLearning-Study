import cv2

image = cv2.imread("bonobono3.png")

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 해당 numpy객체의 특정 픽셀을 가져온다
px = image[100,100]

# B, G ,R 순으로 출력
# gray형태는 좀 다르게 출력된다
print(px)

# R값만 출력하기
print(px[2])

# 특정 범위 픽셀 변경
image[0:100, 0:100] = [0,0,0]
cv2.imshow("image",image)
cv2.waitKey(0)

# ROI: Region Of interest: 특정 이미지에서 유의미한 feature 를 가지는 공간
roi = image[150:300,150:300]
image[0:150, 0:150] = roi
cv2.imshow("image",image)
cv2.waitKey(0)

# 픽셀별로 색상 다루기
image[:,:,2] = 0
cv2.imshow("image",image)
cv2.waitKey(0)