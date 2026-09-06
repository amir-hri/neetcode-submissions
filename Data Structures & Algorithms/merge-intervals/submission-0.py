class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        output = [intervals[0]]

        for i in range(1, n):
            curr = intervals[i]
            last = output[-1]

            if curr[0]<=last[1]:
                last[1] = max(curr[1], last[1])
            else:
                output.append(curr)
        return output

