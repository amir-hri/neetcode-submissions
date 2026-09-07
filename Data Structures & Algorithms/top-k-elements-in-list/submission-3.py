class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        o = []
        n = len(nums)
        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0)+1
        while k>=1:
            ind = -1
            curr = max(d.values())
            for key in list(d.keys()):
                if d[key]==curr:
                    ind = key
                    del d[key]
                    break
            o.append(ind)

            k-=1
        return o