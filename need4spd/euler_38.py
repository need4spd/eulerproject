def isPandigital(n):
  if (len(n) == 9):
    temp_l = ''.join(sorted([ c for c in n]))
    if temp_l == '123456789':
      return True;
  return False
  

result = 0
for n in range(9183, 9877):
  a1 = str(n * 1) + str(n * 2)
  if isPandigital(a1):
    if result < int(a1):
      result = int(a1)

print (result)