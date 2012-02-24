result = 0

def fac(x):
	for a in range(2,x):
		if x % a == 0:
			result = a
			print(x,a,x//a)
			return fac(x//a)

print(fac(600851475143))
