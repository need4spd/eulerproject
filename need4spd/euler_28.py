sum=1
rows=1002

for n in range(3, 1002, 2):
    up_r = n**2
    up_l = up_r - (n-1)
    dn_l = up_l - (n-1)
    dn_r = dn_l - (n-1)
    
    print(up_r, up_l, dn_l, dn_r)
    sum = sum + up_r + up_l + dn_l + dn_r

print(sum)