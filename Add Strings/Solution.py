class Solution:
    def addStrings(self, num1: str, num2: str) -> str:      
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1
        res = []
        carry = 0
        
        while pointer1 >= 0 or pointer2 >= 0:
            numb1 = ord(num1[pointer1]) - ord("0") if pointer1 >=0 else 0
            numb2 = ord(num2[pointer2]) - ord("0") if pointer2 >=0 else 0
            
            value = (numb1 + numb2 + carry) % 10
            carry = (numb1 + numb2 + carry) // 10
            
            res.append(value)
            
            pointer1 -= 1
            pointer2 -= 1
            
        if carry:
            res.append(carry)
            
        
        return "".join(chr(ord("0") + x) for x in res[::-1])