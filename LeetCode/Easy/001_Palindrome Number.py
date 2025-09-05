class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x=0
        ori=x
        while x>0:
            last_digit = x%10
            reversed_x = (reversed_x*10)+last_digit
            x//=10
        return reversed_x==ori
        
sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))