def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = 1
while True:
    r = fib(n)
    
    if len(str(r)) == 1000:
        print(n)
        break
    
    n+=1