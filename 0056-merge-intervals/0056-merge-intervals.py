class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        li = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= li[-1][-1]:
                if intervals[i][-1] > li[-1][-1]:
                    li[-1][-1] = intervals[i][-1]
                else:
                    li[-1][-1] =li[-1][-1]
                
            else:
                li.append(intervals[i])
        return li