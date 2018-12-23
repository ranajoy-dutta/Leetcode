class Solution:
    def strStr(self, haystack, needle):
        length = len(needle)
        if length == 0:
            return 0
        pos = -1
        for i in range(len(haystack)-length+1):
            print(haystack[i:i+length])
            if haystack[i:i+length] == needle:
                return i
        return pos