def multiple(a):
	if a%3 == 0 or a%5 == 0:
		return a
	else:
		return 0

number = range(1,1000)
c=0
for a in number:
	c = c+multiple(a)

print(c)