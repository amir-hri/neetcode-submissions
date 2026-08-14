class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for char in s:
                if char in t:
                    s=s.replace(char,"",1)
                    t=t.replace(char,"",1)
                else:
                    return False
            return True
