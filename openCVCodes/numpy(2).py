import numpy as np

# 배열의 상수연산
array = np.random.randint(1,10,size=4).reshape(2,2)
print(array)
result_array = array * 10
print(result_array)

# numpy는 서로 다른 형태의 배열의 계산이 가능하게 한다 = broadcasting
array1 = np.arange(4).reshape(2,2)
array2 = np.arange(2)

array3 = array1 + array2
print(array3)

# 브로드캐스팅 연습     -> 4 * 1 형태의 경우 4 * 4형태로 확장을 시켜준다
array4 = np.arange(0,8).reshape(2,4)
array5 = np.arange(0,8).reshape(2,4)
array6 = np.concatenate([array4, array5], axis=0)
array7 = np.arange(0,4).reshape(4,1)

print(array6 + array7)

# 마스킹 연산 = 각 원소에 대해 특정 조건이 맞는지 체크하는 함수
# 마스킹을 사용하여서 특정 조건을 만족하는 부분에만 특정 행동을 취할 수 있게 된다
array8 = np.arange(16).reshape(4,4)
array9 = array8 < 10
print(array9)

array8[array9] = 100        # true가 된 부분에만 값을 100으로 만들어준다    -> 픽셀 값 등을 바꿔줄 떄 잘 사용할 수 있다.
print(array8)

# 집계함수
array10 = np.arange(16).reshape(4,4)
print("최댓값: ", np.max(array10))
print("최솟값: ", np.min(array10))
print("합계: ", np.sum(array10))
print("평균: ",np.mean(array10))
print("각 열의 합계: ", np.sum(array10, axis=0))     # 행을 나눈다고 이해하면 되련가?
