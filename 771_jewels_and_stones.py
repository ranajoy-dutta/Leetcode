class Solution:
    def numJewelsInStones(self, J, S):
        jewel = len(J)-1
        stone = len(S)
        count = 0
        while jewel >= 0:
            for i in range(stone):
                if S[i] == J[jewel]:
                    count += 1
            jewel -= 1
        return count