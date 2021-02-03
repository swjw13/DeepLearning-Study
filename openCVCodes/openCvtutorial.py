import cv2

# 각 함수의 flag값을 바꿔주면서 여러가지 기능을 넣어줄 수 있을 거 같다
img_basic = cv2.imread("bonobono3.png", cv2.IMREAD_COLOR)   # color를 입혀서 출력하겠다
cv2.imshow("Image Basic", img_basic)
cv2.waitKey(0)
cv2.imwrite("bon.jpg",img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)      # 이미지를 흑백으로 바꿔주는 코드
cv2.imshow("Image Basic", img_gray)
cv2.waitKey(0)