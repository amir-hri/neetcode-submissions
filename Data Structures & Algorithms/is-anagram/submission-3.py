class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                chars = s[i]
                chart = t[i]
                count[ord(chars)-ord('a')]+=1
                count[ord(chart)-ord('a')]-=1
            for c in count:
                if c!=0:
                    return False
            return True
