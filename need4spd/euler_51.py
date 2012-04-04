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

max = 100000
min = 10000
#prime_list = [int(n) for n in range(min, max) if isPrime(n)]
#patterns = ['110001','101001','100101','100011','011001','010101','010011','001101','001011','000111']
patterns = ['11001','10101','10011','10001','10111','11011','11101']
prime_list = [56003]

for p in prime_list:
  cnt = 0
  replace_num_list = []
  
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
      
      if not replace_num in replace_num_list:
        replace_num_list.append(replace_num)
  print (replace_num_list)
      
  for n in replace_num_list:
    if isPrime(n) and int(n) > 9999:
      print (p, n, int(n))
      cnt += 1 
  
  if cnt == 6:
    print ("result : ", p)