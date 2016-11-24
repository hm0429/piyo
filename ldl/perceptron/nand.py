def NAND(x1, x2):
	w1, w2, theta = -0.5, -0.5, -1.0
	tmp = x1*w1 + x2*w2
	if tmp <= theta:
		return 0
	else:
		return 1

print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))
