def check_cycle(d):
    remain_list = list()
    dividend = 1
    n = 0
    while True:
        remain = dividend % d # 나머지
        
        if remain in remain_list:
            return n - remain_list.index(remain)
        else:
            remain_list.append(remain)
            dividend = remain * 10
            n += 1

max_d = 0
d = 2
max_n = 0
while d < 1000: 
    temp = check_cycle(d)
    if temp > max_n:
        max_n = temp
        max_d = d 
    d += 1
 
print(max_d)