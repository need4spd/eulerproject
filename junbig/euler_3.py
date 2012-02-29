a = 600851475143
b = [0]
count = 2
while a > 0 :
  if a % count == 0:
    a = a / count

    b.append(count)
    if ( a == 1) :
      break
  else :
    count = count + 1

print(max(b))
