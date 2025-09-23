class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        num = 0
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
            
        num_min,num_max = -(2**31), 2**31 - 1
        
        for i in s:
            if not i.isdigit():  
                break
            num = 10*num + (ord(i)-ord('0'))
        num*=sign

        if num<num_min:
            return num_min
        if num>num_max:
            return num_max

        return num