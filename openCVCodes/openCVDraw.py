import cv2
import numpy as np

image = np.full((512,512,3),255, np.uint8)          # full((가로,세로,색깔 갯수), 전체 색깔, 8bit)
image = cv2.line(image, (0,0), (255,255), (255,0,0), 10)        #(그릴 객체, 시작점, 끝점, 색깔, 두께)

cv2.imshow("Image", image)
cv2.waitKey(0)

#직사각형그리기
image2 = cv2.rectangle(image, (20,20), (255,255), (0,0,255), -1)    # -1: 내부를 모두 채워줌
cv2.imshow("Image", image2)
cv2.waitKey(0)

#원 그리기
image3 = cv2.circle(image,(255,255), 30, (0,255,0), 3)
cv2.imshow("Image", image3)
cv2.waitKey(0)

# 다각형 그리기
points = np.array([[5,5],[128,256],[483,444],[400,155]])
image4 = cv2.polylines(image, [points], True, (0,0,255),4)      # True부분: isClosed
cv2.imshow("Image", image4)
cv2.waitKey(0)

#텍스트 그리기
image5 = cv2.putText(image, "Helloworld!", (0,300), cv2.FONT_ITALIC, 2, (255,255,0))
cv2.imshow("Image", image5)
cv2.waitKey(0)