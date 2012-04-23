max_loop_cnt = 49
"""
349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337
"""

def isPalindrome(n):
    n_str = str(n)
    reverse_str = n_str[::-1]
     
    return n_str == reverse_str
 
result=0

for n in range(1, 10001):
  loop_cnt = 0
  while(True):
    if loop_cnt == max_loop_cnt:
      break
    reverse_n = str(n)[::-1]
    n = n +  int(reverse_n)
    
    #print (n, reverse_n)
    
    if isPalindrome(n) and len(str(n)) > 1:
      #print("palindorem..."+str(n))
      result += 1
      break
      
    loop_cnt += 1

print (10000 - result)