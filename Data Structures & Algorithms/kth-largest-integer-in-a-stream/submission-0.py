class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        temp = self.nums.copy()
        for i in range(self.k):
            curr = max(temp)
            temp.remove(curr)
        return curr
