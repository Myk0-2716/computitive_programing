class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merge = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= merge[-1][-1]:
                if intervals[i][-1] <= merge[-1][-1]:
                    merge[-1][-1] = merge[-1][-1]
                else:
                    merge[-1][-1] = intervals[i][-1]
            else:
                merge.append(intervals[i])
        return merge
        