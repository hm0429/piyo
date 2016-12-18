import numpy as np
import matplotlib.pylab as mpl

## オーバフロー対策がされていないsoftmax関数
def softmax(a):
	exp_a = np.exp(a)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

## オーバフロー対策済みのsoftmax関数
def softmax2(a):
	c = np.max(a)
	exp_a = np.exp(a - c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)

## オーバーフローする例	
# a = np.array([1010, 1000, 990])
# y = softmax(a)
# print(y)

## オーバーフロー対策済みのsofmax2関数を使用	
a = np.array([1010, 1000, 990])
y = softmax2(a)
print(y)
