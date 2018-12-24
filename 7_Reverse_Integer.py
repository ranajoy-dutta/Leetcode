import math
class Solution:
    def reverse(self, x):
        orig=x
        num=0
        x=abs(x)
        while x>0:
            try:
                num = num * 10 + x % 10
                x=math.floor(x / 10)
            except:
                break
        if num>math.pow(2, 31):
            return 0
        if orig<0:
            return(num-2*num)
        else:
            return(num)