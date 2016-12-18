import numpy as np
def mean_squared_error(y, t):
	return 0.5 * np.sum((y-t)**2)

## 正解は index == 2
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

## 得られた回答。index == 2 (0.6) の確率が一番高い	
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

## エラー率（誤差が少ない）
error = mean_squared_error(np.array(y), np.array(t))
print(error)


## 得られた回答。index == 7 (0.6) の確率が一番高い	
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

## エラー率（誤差が多い）
error = mean_squared_error(np.array(y), np.array(t))
print(error)