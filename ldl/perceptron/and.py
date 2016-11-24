def AND(x1, x2):
	w1, w2, theta = 1.0, 1.0, 1.0
	tmp = x1*w1 + x2*w2
	if tmp <= theta:
		return 0
	else:
		return 1

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
