import math

a=math.factorial(100)
a=str(int(a))
l=list()
l+=a
print(sum([int(i) for i in l]))