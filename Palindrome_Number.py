import math
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            num = 0
            orig = x
            while x>0:
                num = num*10 + x%10
                x = math.floor(x/10)
            if num == orig:
                return True
            else:
                return False
        