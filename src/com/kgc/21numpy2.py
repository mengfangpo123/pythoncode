import numpy as np
# array=np.random.randint(1,10,20).reshape(4,5)
# print(array)
# for i in range(0,array.shape[0]):
#     for j in range(0,array.shape[1]):
#         print(array[i][j],end="\t")
#     print()
# print(array.sum())
# print(array.sum(0))
# print(array.sum(1))
# array2=np.ones(20).reshape(5,4)
# print(array+array2)
# print(array-array2)
# ji=np.dot(array,array2)
# print(ji)
array=np.random.randint(1,10,9).reshape(3,3,)
print(array)
# inv = np.linalg.inv(array)
# array2=np.dot(inv,array)
array2=np.ones(9).reshape(3,3)
# print(np.vstack((array,array2)))
# print(np.hstack((array,array2)))
# print(np.ravel(array))
# array3=np.stack((array,array2),2)
# print(array3)
# print(array3.ndim)
# print(array3.shape)
print(np.split(array,3))