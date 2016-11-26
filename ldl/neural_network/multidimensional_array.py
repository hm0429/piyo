import numpy as np

def array_info(arr):
	print("==============================")
	print(arr)
	print(np.ndim(arr),"dimensional array")			## 配列の次元数を取得
	print(arr.shape)			## 配列の形状を取得
	print("==============================")

## 1次元の配列
A = np.array([1 , 2, 3, 4])
array_info(A)

## 2次元配列
B = np.array([[1,2], [3,4], [5,6]])
array_info(B)


