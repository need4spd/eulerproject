import time

def LCM(arr):
    resultNum = min(arr)
    totalNum = 0
    
    while(True):
        resultNum += 1
        if( sum(resultNum%x for x in arr) == 0 ):
            break
    
    return resultNum

arr = list(range(1, 21))
start = time.time()

while(True):
    #print(arr)
    if(len(arr) > 3):
        lcm = LCM(arr[0:4])
        #print(str(arr[0]) + "  " + str(arr[1]) + "  " + str(lcm))
        for i in range(3): arr.pop(0)
        arr[0] = lcm
        
    else:
        break
        
print("resultNumber : " + str(arr[0]))
print("running time : " + str(time.time() - start))
