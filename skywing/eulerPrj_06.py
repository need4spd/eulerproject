def eulerPrj06(n):
    arr = range(1, n+1)
    totSqrtFirst = sum([pow(x, 2) for x in arr])
    totSumFirst = pow(sum(arr), 2)
    
    print("totSqrtFirst : " + str(totSqrtFirst))
    print("totSumFirst : " + str(totSumFirst))
    print("totSumFirst - totSqrtFirst : " + str(totSumFirst - totSqrtFirst))
    
eulerPrj06(100)