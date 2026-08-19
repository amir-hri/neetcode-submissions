class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = []
        for s in strs:
            encoded_s.append(str(len(s)))
            encoded_s.append("#")
            encoded_s.append(s)
        return ''.join(encoded_s)
                
                
    def decode(self, s: str) -> List[str]:
        decoded_s = []
        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j += 1
            l = int(s[i:j])
            i = j+1
            j = i+l
            decoded_s.append(s[i:j])
            i=j
        return decoded_s


