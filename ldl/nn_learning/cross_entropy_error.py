import numpy as np

def cross_entropy_error(y, t):
	delta = 1e-7
	return -np.sum(t * np.log(y + delta))

## 正解は index == 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

## 得られた回答。index == 2 (0.6) の確率が一番高い	
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

## エラー率（誤差が少ない）
error = cross_entropy_error(np.array(y), np.array(t))
print(error)


## 得られた回答。index == 7 (0.6) の確率が一番高い	
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

## エラー率（誤差が多い）
error = cross_entropy_error(np.array(y), np.array(t))
print(error)