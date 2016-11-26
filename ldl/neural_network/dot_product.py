import numpy as np

def array_info(arr):
	print("==============================")
	print(arr)
	print(np.ndim(arr),"dimensional array")			## 配列の次元数を取得
	print(arr.shape)			## 配列の形状を取得
	print("==============================")

## [2x2] x [2x2]
A = np.array([[1,2], [3,4]])
array_info(A)

B = np.array([[5,6], [7,8]])
array_info(B)

AB = np.dot(A, B)
array_info(AB)

## [2x3] x [3x2]
C = np.array([[1,2,3], [4,5,6]])
array_info(C)

D = np.array([[1,2], [3,4], [5,6]])
array_info(D)

CD = np.dot(C, D)
array_info(CD)

## [3x2] x 2 ([3x2] x [2x1])
E = np.array([[1,2], [3,4], [5,6]])
array_info(E)

F = np.array([7,8])
array_info(F)

EF = np.dot(E, F)
array_info(EF)



