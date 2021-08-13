def myAtoi(self, s: str) -> int:
    s = s.lstrip()
    op = 0
    flag = True
    starter = 1

    if s == "":
        return 0    
        
    list1 = list(s)
    
    if list1[0] == '-': 
        flag = False
    elif list1[0] == '+':
        flag = True
    else:
        flag = True
        starter = 0
    
    digits = []
    for i in list1[starter:]:
        if ord(i) in range(48,58):
            digits.append(int(i))
        else: 
            break
    
    for digit in digits:
        op = op * 10 + digit
        
    if not flag:
        op = -op
        if (op < (-2**31)):
            return -2**31
    
    if (op > (2**31 - 1)):
        return 2**31 - 1
    else:
        return op

myAtoi("42")
myAtoi("   -42")
myAtoi("4193 with words")
myAtoi("words and 987")
myAtoi("-91283472332")
myAtoi("+1")
myAtoi("+-2")
myAtoi("-+1")
myAtoi("")
myAtoi("2147483648")
