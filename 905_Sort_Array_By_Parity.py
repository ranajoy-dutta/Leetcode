'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

class Solution:
    def sortArrayByParity(self, A):

        n = len(A)
        B=[0]*n
        start, end = 0, n-1

        for i in range(n):
            if A[i]%2==0:
                B[start]=A[i]
                start+=1
            else:
                B[end]=A[i]
                end-=1
        return B
        