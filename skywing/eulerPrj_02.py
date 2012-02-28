
total = 0
prevNum = 1
nextNum = 2

while (prevNum < 4000000):
    temp = prevNum
    prevNum = nextNum
    nextNum = temp+nextNum
    
    if prevNum%2 == 0:
        total += prevNum

print(total)