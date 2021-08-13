class Solution:
    def myAtoi(self, s: str) -> int:
        op = 0
        flag = True

        s = s.lstrip()

        if len(s) == 0: return 0    
            
        list1 = list(s)
        
        if list1[0] == '-': 
            flag = False
            list1 = list1[1:]
        elif list1[0] == '+':
            flag = True
            list1 = list1[1:]
        else:
            flag = True    
    
        for i in list1:
            if i.isdigit():
                op = op * 10 + int(i)
            else: 
                break
            
        if not flag:
            op = -op
            if (op < (-2147483648)):
                return -2147483648
        
        if (op > (2147483647)):
            return 2147483647
        else:
            return op    