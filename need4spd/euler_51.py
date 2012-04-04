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
min = 100000
prime_list = [int(n) for n in range(min, max) if isPrime(n)]
patterns = ['110001','101001','100101','100011','011001','010101','010011','001101','001011','000111']


for p in prime_list:
  cnt = 0
  for i in range(0,10):
    for pat in patterns:
      replace_num = ""
      
      p_index = 0
      for c in pat:
        if c == str(1):
          replace_num = replace_num + str(p)[p_index]
        else:
          replace_num = replace_num + str(i)
        p_index += 1
      
      if isPrime(replace_num) and int(replace_num) > 99999:
        print (p, replace_num, int(replace_num), pat, i)
        cnt += 1 
  if cnt == 8:
    print (p)