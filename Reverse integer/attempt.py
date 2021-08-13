def reverse(x: int) -> int:
    rev = 0
    orig = x
    if orig < 0:
        x = -x
    
    while (x != 0):
        rev = (rev * 10) + (x % 10)
        x = int(x/10)
        
    if orig < 0 :
        rev = -rev
    
    if (rev > 2**31 - 1 or rev < -2**31):
        return 0
        
    return rev

print(reverse(x=567))
print(reverse(x=-1256))
