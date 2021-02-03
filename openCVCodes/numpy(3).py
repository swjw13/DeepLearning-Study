import numpy as np

# 단을 객체 저장 및 불러오기
array = np.arange(0,10)
np.save("saved.npy", array)

result = np.load("saved.npy")
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(10)
array2 = np.arange(10,20)
np.savez("saved.npz", array1 = array1, array2 = array2)
data = np.load("saved.npz")
print(data['array1'])
print(data['array2'])

# 원소의 정렬
array3 = np.array([5,9,10,3,1])
array3.sort()
print(array3)
print(array3[::-1])

# 각 열을 기준으로 정렬      -> 각 열을 오름차순으로 정렬
array4 = np.array([[5,9,10,3,1],[8,3,4,2,5]])
array4.sort(axis=0)
print(array4)

# 균일한 간격으로 데이터 생성
array5 = np.linspace(0,10,5)
print(array5)

# 난수의 재현(실행마다 결과 동일)
np.random.seed(7)   # 난수를 지정해줘서 항상 랜덤 값을 같게 해 준다
print(np.random.randint(0,10,(2,3)))

# numpy 배열 객체 복사
array6 = np.arange(10)
array7 = array1
array[2] = 100      # array6의 값도 바뀐다

array8 = array6.copy()      # array를 그대로 복사한다(주솟값이 달라짐)

# 중복된 원소 제거
array9 = np.array([1,2,2,3,1,1,4])
print(np.unique(array9))