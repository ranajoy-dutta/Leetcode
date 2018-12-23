class Solution:
    def removeDuplicates(self, nums):
        pos = 0
        while pos < len(nums)-1:
            if nums[pos] == nums[pos+1]:
                del nums[pos+1]
            else:
                pos += 1
        return len(nums)
 