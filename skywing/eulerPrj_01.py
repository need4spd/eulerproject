maxNum = range(1,1000)
total = 0

for i in maxNum:
    if i%3 == 0 or i%5 == 0:
        total += i
        
print('Total Sum : ' + str(total))

    