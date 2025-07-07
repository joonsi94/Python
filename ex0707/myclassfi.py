# 머신러닝 - 정형화데이터 숫자

#딥러닝 - 비정형화 데이터 음성,이미지,영상

#AI > 머신러닝 > 딥러닝

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

a_x = [3,4,5,6,7]
a_y = [12,14,11,13,10]

b_x = [20,21,22,23,24]
b_y = [21,22,32,21,23]

c_x = [4,3,1,5,3]
c_y = [1,2,3,1,5]

d_x = [14,13,21,15,43]
d_y = [1,2,3,1,5]

xx = a_x+b_x+c_x+d_x
yy = a_y+b_y+c_y+d_y

data = [[x,y] for x,y in zip(xx,yy)]
target = [0]*5 + [1]*5 + [2]*5 + [3]*5
print(data)
print(target)

#최근접이웃모델가져와라
kn = KNeighborsClassifier()
#학습해라
kn.fit(data,target)

#예측
result = kn.predict([[3,5],[2,7]])
print(result)



# plt.scatter(a_x,a_y)
# plt.scatter(b_x,b_y)
# plt.scatter(c_x,c_y)
# plt.scatter(d_x,d_y)
# plt.scatter([3,2],[5,7])
# plt.show()

# 최근접 이웃 알고리즘 숫자 입력들어오면
