def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

max = 1000000
prime_list = [int(n) for n in range(2, max+1) if isPrime(n)]

terms = 0
temp_r = 0
result = 0

[2,3,5,7,11,13,17,19,23,29,31...]
[2,5,10,17,28,41,58,77,100]
1) index ~ n까지의 합은
sum(n) - prime_list[index]와 같다.