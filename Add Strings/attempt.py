class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        mapping = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        
        numb1 = 0
        numb2 = 0
        op = []
        
        for digit in num1:
            numb1 = (numb1 * 10) + mapping[digit]
            
        for digit in num2:
            numb2 = (numb2 * 10) + mapping[digit]
            
        print(numb1)
        print(numb2)
        
        res = numb1 + numb2
        
        if numb1 + numb2 == 0:
            return "0"
        
        while res > 0:
            print(res)
            digit = res % 10
            # Fails here because digit division fails as it res crosses sys.maxint
            res = int(res / 10)
            
            digit_str = list(mapping.keys())[list(mapping.values()).index(digit)]      
            
            op.insert(0, digit_str)
                        
        return "".join(op)
            