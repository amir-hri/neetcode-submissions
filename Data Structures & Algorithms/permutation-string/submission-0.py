from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        w = len(s1)
        if w>n:
            return False
        target = Counter(s1)
        window = Counter(s2[:w])
        if target==window:
            return True
        for r in range(w, n):
            window[s2[r]]+=1
            left=s2[r-w]
            window[left]-=1
            if window[left]==0:
                del window[left]
            if target==window:
                return True
        return False
