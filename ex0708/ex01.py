a = [1,2,3,4,5]
b = [4,5,6,7,8]

import numpy as np

na = np.array([1,2,3,4,5])
nb = np.array([4,5,6,7,8])

#슬라이싱 문법
print(a[:3])
print(na[:2])

print(a+b)
print(na+nb)

#print(a*b) # 기본 배열은 파이썬에서 행열 곱셈 허용 X
print(na*nb) #umpy 배열은 파이썬에서 행열 곱을 허용 O