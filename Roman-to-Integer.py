"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I              1
V              5
X              10
L              50
C              100
D              500
M              1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4
"""

class Solution:
    def toInt(self,i):
        if i == 'M':
            return 1000
        elif i == 'D':
            return 500
        elif i == 'C':
            return 100
        elif i == 'L':
            return 50
        elif i == 'X':
            return 10
        elif i == 'V':
            return 5
        elif i == 'I':
            return 1
        
    def romanToInt(self, s):
        s=list(s)
        summ=0
        flag=0
        for i in range(len(s)):
            current = self.toInt(s[i])
            if flag == 1:
                flag = 0
                continue
            if i+1 < len(s):
                print('current : ',current)
                nextt = self.toInt(s[i+1])
                print('next : ',nextt)
                if nextt <= current:
                    summ += current
                    print(i,summ)
                else:
                    summ = summ + nextt - current
                    flag = 1
                    print("***",i,summ)
            else:
                summ += current
                print('else',summ,current)
        return summ
