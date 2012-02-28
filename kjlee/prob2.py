#prob2.py : fibonacci

f=[1,2]
result = 0
tmp = 0

while f[0]+f[1] <= 4000000 :
	sum = f[0]+f[1]
	tmp = f[0]
	f[0] = f[1]
	f[1] = tmp + f[1]

	if sum % 2 == 0:
		result = result + sum


print(result + 2)
