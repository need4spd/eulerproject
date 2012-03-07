#prob5.py: lcm
 
def gcd(a,b):
    for i in range(a*b,0,-1):
        if a%i==0 and b%i==0:
            return i

def lcm(a,b):
    if a == b or b%a == 0:
        return b

    mul = (int)(a*b/gcd(a,b))

    while 1:
        if mul%a==0 and mul%b==0:
                return mul
        else:
            mul += 1


v_lcm = 2
for i in range(1,20):
    v_lcm = lcm(i, v_lcm)
    print(v_lcm)
