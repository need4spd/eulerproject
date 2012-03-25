import math
 
def is_pentagonal(n):
  n = abs(n)
  p = ( math.sqrt(1 + 24*n) + 1 ) / 6
  return p==int(p)

pent_list = [1]

i = 0
not_found = True
while not_found:
  i+=1
  
  pent_list.append(int(i * (3*i - 1)/2))
  
  for j in range(2, len(pent_list) - 1):
    if is_pentagonal(pent_list[i] - pent_list[j]) and is_pentagonal(pent_list[i] + pent_list[j]):
      print (pent_list[i] - pent_list[j])
      not_found = False
      break
