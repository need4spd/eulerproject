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
primes = [int(n) for n in range(2, 1000001) if isPrime(n)]
prime_sum = [0]
 
sum = 0
count = 0
while (sum < max):
  sum+=primes[count]
  prime_sum.append(sum)
  count+=1

print (prime_sum, count)

terms = 1
max_prime=0
for i in range(count):
  for j in range(i+terms, count):
    n = prime_sum[j] - prime_sum[i]
    
    print ("i={0}, j={1}, terms={2}, max_prime={3}, n={4}, isPrime={5}, j-i={6}".format(i,j,terms,max_prime,n,isPrime(n),j-i > terms))
    if (j-i>terms and isPrime(n)):
      (terms,max_prime) = (j-i,n)
 
print ("Answer to Problem 50 = ",max_prime," with ",terms," terms\n");
