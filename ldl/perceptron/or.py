def OR(x1, x2):
	w1, w2, theta = 1.5, 1.5, 1.0
	tmp = x1*w1 + x2*w2
	if tmp <= theta:
		return 0
	else:
		return 1

print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))
