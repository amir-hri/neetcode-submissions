class Solution:
    def isValid(self, s: str) -> bool:
        openP = ['(','[','{']
        closeP = [')',']','}']
        valids = ['()','[]','{}']
        stack = []
        for p in s:
            if p in openP:
                stack.append(p)
            if p in closeP:
                if not stack:
                    return False
                if stack.pop()+p not in valids:
                    return False
        return not stack
