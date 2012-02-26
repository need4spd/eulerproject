array = [1,2]
sum = 0
while array[1] < 4000000:
	if array[1] % 2 == 0:
		sum += array[1]
	
	array.append(array[0] + array[1])
	array.remove(array[0])
print(sum)
