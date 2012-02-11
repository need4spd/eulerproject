import math
def fn(n):
    '''returns number of factors of an integer'''
    count = 0
    i = 1
    while i <= math.sqrt(n):
        if n%i == 0:
            count += 2
        i += 1
    return count

def tr(n):
    '''returns nth triangle number'''
    tri = 0
    i = 0
    while i < n+1:
        tri += i
        i += 1
    return tri    
i = 1
while True:
    if fn(tr(i)) > 500:
        break
    else:
        i += 1
print (tr(i))
print (i)