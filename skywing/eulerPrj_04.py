def MaxSymmetryNumber(n):
    rangeMinNum = pow(10,n-1)    
    rangeMaxNum = pow(10,n)
    
    number1 = range(rangeMaxNum, rangeMinNum, -1)
    number2 = range(rangeMaxNum, rangeMinNum, -1)
    symmetryNumberList = list()
    
    for i in number1:
        for j in number2:
            multiNum = str(i*j)
            reverseNum = multiNum[::-1]
            #reverseNum = ''.join(reversed(multiNum))
            
            if( multiNum == reverseNum ):
                #print(str(i) + "*" + str(j) + "=" + multiNum)
                symmetryNumberList.append([int(multiNum), i, j])
                #return
    
    return max(symmetryNumberList)

a = MaxSymmetryNumber(3)
print(a)
