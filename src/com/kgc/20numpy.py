# 创建矩阵
import numpy as np
# array = np.array([1,2,3])
# array = np.array([[1,2],[3,4]])
# array=np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]],[[13,14],[15,16]]])
# array=np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]],[[[17,18],[19,20]],[[21,22],[23,24]]]])
# print(array)
# array = np.array([[[[1,2],[3,4]],[[1,2],[3,4]]],[[[1,2],[3,4]],[[1,2],[3,4]]]])
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)
#
# array = np.arange(1,10).reshape(3,3)
# print(array)
# print(array.ndim)
# np.random.randint()
array=np.random.randint(1,10,16).reshape(4,4)
print(array)
# print(array[2][2])
# print(array[0])
# print(array[:,0])
# print(array[0:3:2])
# print(array[::,1::2])
print(array[0:3:2,1::2])

