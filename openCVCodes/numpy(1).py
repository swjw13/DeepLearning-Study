import numpy as np

list = [1,2,3]
array = np.array(list)  # numpy형 데이터로 바꾸어서 여러 내부 함수들로 사용할 수 있다

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

array2 = np.zeros((4,4), dtype=float)   # 4 * 4 크기의 배열, 0으로 초기화, datatype = float
print(array2)

array3 = np.ones((3,3), dtype=str)  # 1로 초기화
print(array3)

array4 = np.random.randint(0,10,(3,3))  ## 랜덤한 값으로 지정해 줌
print(array4)

# 특정한 분포를 가지는 형태로 만들 수 있음
# 평균이 0이고 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0,1,(3,3))
print(array5)

# 두 배열을 합칠 수 있다
array6 = np.array([1,2,3])
array7 = np.array([4,5,6])
array8 = np.concatenate([array6, array7])
print(array8.shape)     # 배열의 크기
print(array8)

# 배열의 형태를 바꿀 수 있다
array9 = np.array([1,2,3,4])
array10 = array9.reshape((2,2))
print(array10)

# 두 배열을 세로로 합칠 수도 있다
array11 = np.arange(4).reshape(1,4)
array12 = np.arange(8).reshape(2,4)
print(array11)
print(array12)

array13 = np.concatenate([array11, array12], axis=0)    # axis=0: 행, axis=1: 열
print(array13)

# 배열을 두개로나눌 수 있다
array14 = np.arange(8).reshape(2,4)
left, right = np.split(array14, [2], axis=1)
print(left)
print(right)

