def isPalindrome(n):
    n_str = str(n)
    reverse_str = n_str[::-1]
    
    return n_str == reverse_str

result=0

for n in range(0, 1000001):
    n_2 = str(bin(n))[2:]
    
    if not isPalindrome(n):
        continue
    
    if n_2[0:1] == 0:
        continue
    
    if not isPalindrome(n_2):
        continue
    
    result+=n

print(result)