list1 = [0,3,3,5,4,4,3,5,5,4]
list2 = [3,6,6,8,8,7,7,9,8,8]
list3 = [0,0,6,6,5,5,5,7,6,6]
hLen = 7
tLen = 8
aLen = 3
def underH(a):
  if a >= 100:
    return 0
  if a < 10:
    return list1[a]
  elif a < 20:
    return list2[a-10]
  else:
    return list3[int(a/10)] + list1[a%10]


s=0
for x in range(1,1001):
  if x < 100:
    s+=underH(x)
  elif x < 1000:
    s+=list1[int(x/100)] + hLen
    t = x%100
    if t > 0:
      s+=aLen
      s+=underH(t)
  else:
    s+=list1[1]+tLen
print(s)