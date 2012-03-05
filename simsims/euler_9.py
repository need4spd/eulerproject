for a in range(1,999):
  for b in range(1,999):
    c = 1000-a-b
    if c > 0 and c*c == a*a + b*b:
      print(a*b*c)
      break
  if b!=998:
    break