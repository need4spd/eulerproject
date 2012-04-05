def is_permutations(a,b):
  s_a = list(str(a))
  s_a.sort()
  s_b = list(str(b))
  s_b.sort()
 
  if s_a == s_b:
    return True
  else:
    return False


n = 125874
while True:
  if is_permutations(n, n*2) and is_permutations(n, n*3) and is_permutations(n, n*4) and is_permutations(n, n*5) and is_permutations(n, n*6):
    print (n)
  n += 1