import numpy as np

## 入力層
## x1, x2
X = np.array([1,2])
print("X:\n", X)

## 重み
## x1: 1,3,5
## x2: 2,4,6
W = np.array([[1,3,5], [2,4,6]])
print("W:\n", W)

## 出力層
Y = np.dot(X, W)
print("Y:\n", Y)

